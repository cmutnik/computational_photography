# Image Background Removal #
----
## Usage ##
To remove image backgrounds:
1. Pip install modules: `pip install -r requirements.txt`
2. Run python script: `python rm_image_bkgd.py`
3. Use the GUI to
    - Select the input image
    - Select the destination and name for the output image

----
## Troubleshooting ##
If the script errors out, you can download the model from [here.](https://drive.google.com/uc?id=1tCU5MM1LhRgGou5OpmpjBQbSrYIUoYab) and store it in `${HOME}/.u2net/.`

Once the model is stored locally, rerun the script by following steps 2 and 3 above.

----
## Example ##
The following are paired input and outputs:

![](../figs/paintings/flower.jpg)
![](../figs/removed_backgrounds/no_bkgd.png)

![](../figs/paintings/flower_oilpainted.jpg)
![](../figs/removed_backgrounds/flower_oilpainted.png)

<img src="../time_slicing/figs/ab100_runall.jpg" alt="drawing" width="250"/><img src="../figs/removed_backgrounds/timeslice_ab100_runall.png" alt="drawing" width="250"/>

![](../figs/zoom_virtual_backgrounds/IMG_3477_1.jpg)
![](../figs/removed_backgrounds/IMG_3477_1_no_bkgd.png)

![](../figs/zoom_virtual_backgrounds/IMG_3477_1.jpg)
![](../figs/zoom_virtual_backgrounds/IMG_3477_1_no_bkgd_resized.png)

![](../figs/zoom_virtual_backgrounds/IMG_3477_1.jpg)
![](../figs/zoom_virtual_backgrounds/IMG_3477_1_no_bkgd_resized_resized.png)

![](../figs/image_stacking/first_stacked_image.JPG)
![](../figs/removed_backgrounds/first_stacked_image_no_bkgd.png)

![](../figs/image_stacking/first_stacked_image.JPG)
![](../figs/removed_backgrounds/first_stacked_image_no_bkgd_resized.png)

![](../figs/image_stacking/first_stacked_image.JPG)
![](../figs/removed_backgrounds/first_stacked_image_no_bkgd_resized_resized.png)



