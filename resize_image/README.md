# Resize Images #

Python script [`resize.py`](./resize.py) allows resizing of all images in designated directory.

----
## Usage ##

All inputs have set defaults, to see them use:
```sh
python resize.py --help
```

With all arguments defined, and excluding multiple extension types (`*.c` and `*.b` files):
```sh
python resize.py --img_path "./foo/bar/*" --output_dir outputs --scale_factor 0.25 --output_extension jpg --excluded_extensions c --excluded_extensions b
```

Using abbreviations for inputs:
```sh
python resize.py -i "./foo/bar/*" -o herebb -sf 0.5 -oe jpg -ee c -ee b
```

----
## Other Options ##
`python resize.py -h`

```
usage: resize.py [-h] [-i str] [-o str] [-sf float] [-oe str] [-ee list of strings]

Resize Images

optional arguments:
  -h, --help            show this help message and exit
  -i str, --img_path str
                        paths to set of images that need to be resized (default: ./*)
  -o str, --output_dir str
                        dir to save resized image results (default: ./)
  -sf float, --scale_factor float
                        scale factor to multiply image dimensions by (default: 0.25)
  -oe str, --output_extension str
                        extension type of resized image (default: png)
  -ee list of strings, --excluded_extensions list of strings
                        list of str that make consists of file extensions to ignore in
                        img_path dir (default: ["py"])
```

----
----
# TODO #
- [] test `len(image filename list) == len(set(img filname list))`; else: duplicate names will be overwritten
- [] pass in desired dimensions, if scale factor unknown or aspect ratio does not need to be preserved