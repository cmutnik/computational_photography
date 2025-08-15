# 📸 Image Manipulation & Metadata Tool

This script resizes, rotates, reformats, strips metadata, and adds copyright info to images — with an optional **size guard** so adding metadata never increases file size.


To update this README automatically with changes to the argparse CLI, run:
```bash
python manipulate_images_for_web.py --generate_readme > README.md
```


## 🚀 Quick Start

### 1. Resize & Convert to WebP
```bash
python manipulate_images_for_web.py -i "photo.jpg" -o "outdir" -sf 0.5 -oe webp
```

### 2. Remove Metadata, Then Add Copyright
```bash
python manipulate_images_for_web.py -i "photo.jpg" -o "outdir" -m -c
```

### 3. Convert a Folder of PNGs to JPEG
```bash
python manipulate_images_for_web.py -i "images/*.png" -o "outdir" -oe jpg
```


## 📋 Command-line Usage
```bash
python manipulate_images_for_web.py [options]
```


## ⚙️ Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `-h, --help` | str | `` | show this help message and exit |
| `-i, --img_path` | str | `./*` | Glob path(s) to images. (default: ./*) |
| `-o, --output_dir` | str | `./` | Dir to save results. (default: ./) |
| `-s, --out_suffix` | str | `_resized` | Suffix used to distinguish input and output images. (default: _resized) |
| `-sf, --scale_factor` | float | `1.0` | Scale factor for width/height. (default: 1.0) |
| `-oe, --output_extension` | str | `None` | Output extension (e.g., webp, jpg, png). Default keeps original. |
| `-ee, --excluded_extensions` | str | `['py']` | List of extensions to ignore (repeatable). |
| `-r, --rotate_image` | int | `None` | Rotate by degrees (e.g., -90). Default: no rotation. |
| `-m, --metadata_removal_indicator` | flag | `False` | Strip all metadata (EXIF) before saving. |
| `-c, --copyright_indicator` | flag | `False` | Add copyright metadata. |
| `--copyright_text` | str | `copyright (c) 2025 takotime808` | Copyright text to embed. (default: 'copyright (c) 2025 takotime808') |
| `--admin_mode` | flag | `False` | Verbose logging. |
| `--allow_png_quantize` | flag | `False` | If needed, quantize PNG to ≤256 colors to keep size non-increasing. |
| `--png_quantize_colors` | int | `256` | Palette size for PNG quantization (if enabled). (default: 256) |
| `-gr, --generate_readme` | flag | `False` | Generate README.md section for CLI usage. |

## 💡 Examples

### Resize a single image
```bash
python manipulate_images_for_web.py -i "input.jpg" -o "outdir" -sf 0.5 -oe webp
```

### Resize all images in a directory
```bash
python manipulate_images_for_web.py -i "images/*.png" -o "outdir" -sf 0.25 -oe jpg
```

### Rotate an image
```bash
python manipulate_images_for_web.py -i "photo.jpg" -o "outdir" -r -90
```

### Remove all metadata (EXIF)
```bash
python manipulate_images_for_web.py -i "photo.jpg" -o "outdir" -m
```

### Add copyright metadata
```bash
python manipulate_images_for_web.py -i "photo.jpg" -o "outdir" -c --copyright_text "© 2025 MyName"
```

### Remove metadata, then add copyright
```bash
python manipulate_images_for_web.py -i "photo.jpg" -o "outdir" -m -c
```

### Change format without resizing
```bash
python manipulate_images_for_web.py -i "image.png" -o "outdir" -oe jpg
```

### Process multiple patterns at once
```bash
python manipulate_images_for_web.py -i "dir1/*.jpg,dir2/*.png" -o "outdir" -sf 0.8
```

### PNG-only size-safe mode with quantization
```bash
python manipulate_images_for_web.py -i "photo.png" -o "outdir" -c --allow_png_quantize --png_quantize_colors 256
```

### Verbose mode (admin)
```bash
python manipulate_images_for_web.py -i "photo.jpg" -o "outdir" -sf 0.5 -c --admin_mode
```

