# Cartoonify Photo #

----
## Usage ##
To run with default parameters:
`python cartoonify_k_means.py`

Run with modified parameters:
`python cartoonify_k_means.py -l 9 -b 9 -k 12`


----
## Other Options ##
`python cartoonify_k_means.py --help`

```
usage: cartoonify_k_means.py [-h] [-i str] [-o str] [-l int] [-b int] [-k int]

Turn Image into Cartoon

optional arguments:
  -h, --help            show this help message and exit
  -i str, --img_path str
                        paths to input image (default:
                        '../../../figs/zoom_virtual_backgrounds/IMG_3477_1.jpg')
  -o str, --output_dir str
                        dir to save resized image results (default: ../../../figs/paintings/)
  -l int, --line_size int
                        line size to be used (default: 7)
  -b int, --blur_value int
                        blur value to be used (default: 7)
  -k int, --total_color int
                        total colors to be used for k value in k-means (default: 9)
```

----
## Example ##

<img src="../../../figs/zoom_virtual_backgrounds/IMG_3477_1.jpg" width="40%"> <img src="../../../figs/paintings/IMG_3477_1_cartoonified.png" width="40%">