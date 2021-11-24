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
----
# TODO #
- [] test `len(image filename list) == len(set(img filname list))`; else: duplicate names will be overwritten
- [] pass in desired dimensions, if scale factor unknown or aspect ratio does not need to be preserved