# Copyright (c) 2025 takotime808
"""
manipulate_images_for_web.py

Batch image manipulation with size-safe copyright tagging.

Features (superset of your two scripts):
- Glob input (e.g., -i "test/*") and skip certain extensions.
- Resize by scale factor, optional rotation, and format conversion.
- Strip all metadata (EXIF) if requested.
- Add a minimal copyright tag.
- **Size guard**: JPEG/WEBP/PNG outputs are saved so the file size does not
  exceed the original when possible. A true no-op (no edits) will copy bytes
  without re-encoding (no growth).
- Progress bar for processing files.
- Deprecation warnings (like Pillow LANCZOS) suppressed.

Examples
--------
1) Simple convert+resize to WebP:
   python manipulate_images_for_web.py -i "test/*" -o test/. -oe webp -sf 0.5

2) Add copyright but keep size ≤ original:
   python manipulate_images_for_web.py -i "img.jpg" -c -o outdir -oe jpg

3) Remove metadata then add copyright (still size-safe):
   python manipulate_images_for_web.py -i "img.png" -m -c -o outdir
"""
from __future__ import annotations

import argparse, os, io, shutil, warnings
from glob import glob
from typing import List, Optional
from PIL import Image, PngImagePlugin, ImageOps

# --- Suppress deprecation warnings (e.g., Pillow LANCZOS) ---
warnings.filterwarnings("ignore", category=DeprecationWarning)

# tqdm (progress bar) is optional
try:
    from tqdm import tqdm
    _HAS_TQDM = True
except ImportError:
    _HAS_TQDM = False

# piexif is optional (only needed when embedding EXIF for JPEG/WEBP/TIFF)
try:
    import piexif  # type: ignore
except ImportError:
    piexif = None  # allow running when not adding EXIF


# ------------------------- CLI -------------------------
parser = argparse.ArgumentParser(description="Manipulate images and manage metadata (size-safe).")
parser.add_argument("-i", "--img_path", type=str, default=r"./*", metavar="str",
                    help="Glob path(s) to images. (default: ./*)")
parser.add_argument("-o", "--output_dir", type=str, default=r"./", metavar="str",
                    help="Dir to save results. (default: ./)")
parser.add_argument("-s", "--out_suffix", type=str, default=r"_resized", metavar="str",
                    help="Suffix used to distinguish input and output images. (default: _resized)")
parser.add_argument("-sf", "--scale_factor", type=float, default=1.0, metavar="float",
                    help="Scale factor for width/height. (default: 1.0)")
parser.add_argument("-oe", "--output_extension", type=str, default=None, metavar="str",
                    help="Output extension (e.g., webp, jpg, png). Default keeps original.")
parser.add_argument("-ee", "--excluded_extensions", action="append", default=["py"], metavar="ext",
                    help="List of extensions to ignore (repeatable).")
parser.add_argument("-r", "--rotate_image", type=int, default=None, metavar="int",
                    help="Rotate by degrees (e.g., -90). Default: no rotation.")
parser.add_argument("-m", "--metadata_removal_indicator", action="store_true",
                    help="Strip all metadata (EXIF) before saving.")
parser.add_argument("-c", "--copyright_indicator", action="store_true",
                    help="Add copyright metadata.")
parser.add_argument("--copyright_text", type=str, default="copyright (c) 2025 takotime808",
                    help="Copyright text to embed. (default: 'copyright (c) 2025 takotime808')")
parser.add_argument("--admin_mode", action="store_true",
                    help="Verbose logging.")
parser.add_argument("--allow_png_quantize", action="store_true",
                    help="If needed, quantize PNG to ≤256 colors to keep size non-increasing.")
parser.add_argument("--png_quantize_colors", type=int, default=256,
                    help="Palette size for PNG quantization (if enabled). (default: 256)")
parser.add_argument("-gr", "--generate_readme", action="store_true",
                    help="Generate README.md section for CLI usage.")
args = parser.parse_args()


# ---------------- README generation --------------------
def generate_readme_from_parser(parser: argparse.ArgumentParser) -> str:
    """Generate README Markdown for CLI usage from argparse parser."""
    lines = []
    lines.append("# 📸 Image Manipulation & Metadata Tool\n")
    lines.append("This script resizes, rotates, reformats, strips metadata, and adds copyright info to images — with an optional **size guard** so adding metadata never increases file size.\n")
    lines.append("\nTo update this README automatically with changes to the argparse CLI, run:\n```bash\npython manipulate_images_for_web.py --generate_readme > README.md\n```\n\n")

    
    # Quick Start
    lines.append("## 🚀 Quick Start\n")
    lines.append("### 1. Resize & Convert to WebP\n```bash\npython manipulate_images_for_web.py -i \"photo.jpg\" -o \"outdir\" -sf 0.5 -oe webp\n```\n")
    lines.append("### 2. Remove Metadata, Then Add Copyright\n```bash\npython manipulate_images_for_web.py -i \"photo.jpg\" -o \"outdir\" -m -c\n```\n")
    lines.append("### 3. Convert a Folder of PNGs to JPEG\n```bash\npython manipulate_images_for_web.py -i \"images/*.png\" -o \"outdir\" -oe jpg\n```\n")
    
    # Usage
    lines.append("\n## 📋 Command-line Usage\n```bash\npython manipulate_images_for_web.py [options]\n```\n")
    
    # Options Table
    lines.append("\n## ⚙️ Options\n")
    lines.append("| Option | Type | Default | Description |")
    lines.append("|--------|------|---------|-------------|")
    for action in parser._actions:
        if action.option_strings:
            opt = ", ".join(action.option_strings)
            typ = getattr(action.type, "__name__", "flag") if action.type else ("flag" if action.nargs in (0, None) and isinstance(action.default, (bool, type(None))) else "str")
            default = action.default if action.default != argparse.SUPPRESS else ""
            desc = (action.help or "").strip()
            lines.append(f"| `{opt}` | {typ} | `{default}` | {desc} |")
    
    # Examples Section
    lines.append("\n## 💡 Examples\n")
    examples = {
        "Resize a single image": "-i \"input.jpg\" -o \"outdir\" -sf 0.5 -oe webp",
        "Resize all images in a directory": "-i \"images/*.png\" -o \"outdir\" -sf 0.25 -oe jpg",
        "Rotate an image": "-i \"photo.jpg\" -o \"outdir\" -r -90",
        "Remove all metadata (EXIF)": "-i \"photo.jpg\" -o \"outdir\" -m",
        "Add copyright metadata": "-i \"photo.jpg\" -o \"outdir\" -c --copyright_text \"© 2025 MyName\"",
        "Remove metadata, then add copyright": "-i \"photo.jpg\" -o \"outdir\" -m -c",
        "Change format without resizing": "-i \"image.png\" -o \"outdir\" -oe jpg",
        "Process multiple patterns at once": "-i \"dir1/*.jpg,dir2/*.png\" -o \"outdir\" -sf 0.8",
        "PNG-only size-safe mode with quantization": "-i \"photo.png\" -o \"outdir\" -c --allow_png_quantize --png_quantize_colors 256",
        "Verbose mode (admin)": "-i \"photo.jpg\" -o \"outdir\" -sf 0.5 -c --admin_mode",
    }
    for title, cmd in examples.items():
        lines.append(f"### {title}\n```bash\npython manipulate_images_for_web.py {cmd}\n```\n")
    
    return "\n".join(lines)


# ---------------- Utilities ----------------
def log(msg: str):
    if args.admin_mode:
        print(msg)

def make_output_dir_if_it_dne(output_dir: str):
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

def get_list_of_input_images(filepath: str, excluded_extensions: List[str]) -> List[str]:
    files = []
    for path in filepath.split(","):
        files.extend(glob(path.strip()))
    return [
        f for f in files
        if not os.path.isdir(f) and f.split(".")[-1].lower() not in {e.lower() for e in excluded_extensions}
    ]

def resize_image(image: Image.Image, scale_factor: float) -> Image.Image:
    if scale_factor == 1.0:
        return image
    w, h = image.size
    new_size = (max(1, int(w * scale_factor)), max(1, int(h * scale_factor)))
    return image.resize(new_size, Image.Resampling.LANCZOS)  # updated from deprecated

def rotate_image(image: Image.Image, degrees: int) -> Image.Image:
    return image.rotate(degrees, resample=Image.Resampling.BICUBIC, expand=True)

def get_final_output_name(infile: str, output_dir: str, output_extension: Optional[str], out_suffix: Optional[str]) -> str:
    output_dir = output_dir if output_dir.endswith("/") else output_dir + "/"
    basename = os.path.splitext(os.path.basename(infile))[0]
    out_ext = (output_extension or os.path.splitext(infile)[1][1:]).lower()
    return f"{output_dir}{basename}{out_suffix}.{out_ext}"

def strip_all_metadata(img: Image.Image) -> Image.Image:
    img = ImageOps.exif_transpose(img)
    data = list(img.getdata())
    cleaned = Image.new(img.mode, img.size)
    cleaned.putdata(data)
    return cleaned

def build_copyright_exif_bytes(copyright_text: str) -> bytes:
    if piexif is None:
        return b""
    exif_dict = {
        "0th": { piexif.ImageIFD.Copyright: copyright_text.encode("utf-8") },
        "Exif": {},
        "GPS": {},
        "1st": {},
        "thumbnail": None,
    }
    return piexif.dump(exif_dict)

def add_png_text_info(pnginfo: Optional[PngImagePlugin.PngInfo], key: str, value: str) -> PngImagePlugin.PngInfo:
    if pnginfo is None:
        pnginfo = PngImagePlugin.PngInfo()
    pnginfo.add_text(key, value)
    return pnginfo

def get_format_from_ext(ext: str) -> str:
    ext = ext.lower()
    if ext in ("jpg", "jpeg"): return "JPEG"
    if ext == "png": return "PNG"
    if ext == "webp": return "WEBP"
    return ext.upper()


# ---------------- Size Guard Save ----------------
def save_with_size_guard(img, dest_path, out_fmt, orig_filesize, exif_bytes=None,
                         copyright_text_for_png=None, allow_png_quantize=False, png_quantize_colors=256):
    out_fmt = out_fmt.upper()
    def trial_save(image, **kwargs):
        bio = io.BytesIO()
        image.save(bio, **kwargs)
        data = bio.getvalue()
        return data, len(data)

    if out_fmt in ("JPEG", "JPG"):
        image_to_save = img.convert("RGB") if img.mode not in ("RGB", "L") else img
        try:
            data, size = trial_save(image_to_save, format="JPEG", quality="keep", subsampling="keep",
                                    optimize=True, progressive=True, exif=exif_bytes or b"")
            if size <= orig_filesize:
                with open(dest_path, "wb") as f: f.write(data)
                return
        except Exception:
            pass
        low, high = 30, 95
        best_data = None
        while low <= high:
            q = (low + high) // 2
            data, size = trial_save(image_to_save, format="JPEG", quality=q, optimize=True,
                                    progressive=True, subsampling="keep", exif=exif_bytes or b"")
            if size <= orig_filesize:
                best_data = data
                low = q + 1
            else:
                high = q - 1
        if best_data is None:
            data, _ = trial_save(image_to_save, format="JPEG", quality=30, optimize=True,
                                 progressive=True, subsampling="keep", exif=exif_bytes or b"")
            best_data = data
        with open(dest_path, "wb") as f: f.write(best_data)
        return

    if out_fmt == "WEBP":
        image_to_save = img.convert("RGB") if img.mode not in ("RGB", "L") else img
        low, high = 50, 95
        best_data = None
        while low <= high:
            q = (low + high) // 2
            data, size = trial_save(image_to_save, format="WEBP", quality=q, method=6, exact=True,
                                    exif=exif_bytes or b"")
            if size <= orig_filesize:
                best_data = data
                low = q + 1
            else:
                high = q - 1
        if best_data is None:
            data, _ = trial_save(image_to_save, format="WEBP", quality=50, method=6, exact=True,
                                 exif=exif_bytes or b"")
            best_data = data
        with open(dest_path, "wb") as f: f.write(best_data)
        return

    if out_fmt == "PNG":
        pnginfo = None
        if copyright_text_for_png:
            pnginfo = add_png_text_info(None, "Copyright", copyright_text_for_png)
        data, size = trial_save(img, format="PNG", optimize=True, compress_level=9, pnginfo=pnginfo)
        if size <= orig_filesize:
            with open(dest_path, "wb") as f: f.write(data)
            return
        if allow_png_quantize:
            qimg = img.convert("RGBA") if img.mode != "RGBA" else img
            qimg = qimg.quantize(colors=png_quantize_colors, method=Image.MEDIANCUT,
                                 dither=Image.FLOYDSTEINBERG)
            data2, size2 = trial_save(qimg.convert("RGBA"), format="PNG", optimize=True,
                                      compress_level=9, pnginfo=pnginfo)
            if size2 <= orig_filesize or size2 < size:
                with open(dest_path, "wb") as f: f.write(data2)
                return
        with open(dest_path, "wb") as f: f.write(data)
        return

    img.save(dest_path, format=out_fmt, exif=(exif_bytes or b""))


# ---------------- Main ----------------
def process_one_file(infile: str):
    make_output_dir_if_it_dne(args.output_dir)
    out_ext = (args.output_extension or os.path.splitext(infile)[1][1:]).lower()
    out_fmt = get_format_from_ext(out_ext)
    outfile = get_final_output_name(
        infile=infile, 
        output_dir=args.output_dir,
        output_extension=out_ext,
        out_suffix=args.out_suffix)
    orig_size = os.path.getsize(infile)
    img = Image.open(infile); img.load()
    changed = False

    if args.metadata_removal_indicator:
        img = strip_all_metadata(img); changed = True

    if args.scale_factor and args.scale_factor != 1.0:
        img = resize_image(img, args.scale_factor); changed = True

    if args.rotate_image is not None:
        img = rotate_image(img, args.rotate_image); changed = True

    src_ext = os.path.splitext(infile)[1][1:].lower()
    if args.output_extension and args.output_extension.lower() != src_ext:
        changed = True

    if not changed and out_fmt in ("JPEG", "JPG", "PNG", "WEBP"):
        shutil.copy2(infile, outfile)
        return

    exif_bytes = None
    png_c_text = None
    if args.copyright_indicator:
        if out_fmt in ("JPEG", "JPG", "WEBP", "TIFF") and piexif is not None:
            exif_bytes = build_copyright_exif_bytes(args.copyright_text)
        elif out_fmt == "PNG":
            png_c_text = args.copyright_text

    save_with_size_guard(img, outfile, out_fmt, orig_size,
                         exif_bytes=exif_bytes,
                         copyright_text_for_png=png_c_text,
                         allow_png_quantize=args.allow_png_quantize,
                         png_quantize_colors=args.png_quantize_colors)


def main():
    # README generation: print and exit before touching files.
    if args.generate_readme:
        print(generate_readme_from_parser(parser))
        return

    files = get_list_of_input_images(args.img_path, args.excluded_extensions)
    if not files:
        log("No input files matched."); return
    iterator = tqdm(files, desc="Processing images") if _HAS_TQDM else files
    for f in iterator:
        try:
            process_one_file(f)
        except Exception as e:
            log(f"Error processing {f}: {e}")


if __name__ == "__main__":
    main()
