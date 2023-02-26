# Image Background Removal #
----
## Usage ##
To remove image $backgrounds^{1}:$
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
## Examples ##
The following are paired input and outputs:

<img src="../figs/zoom_virtual_backgrounds/IMG_3477_1.jpg" alt="drawing" width="250"/><img src="../figs/removed_backgrounds/IMG_3477_1_no_bkgd.png" alt="drawing" width="250"/>

![](../figs/paintings/flower.jpg)
![](../figs/removed_backgrounds/no_bkgd.png)

![](../figs/paintings/flower_oilpainted.jpg)
![](../figs/removed_backgrounds/flower_oilpainted.png)

<img src="../figs/image_stacking/first_stacked_image.JPG" alt="drawing" width="250"/><img src="../figs/removed_backgrounds/first_stacked_image_no_bkgd_resized.png" alt="drawing" width="250"/>


----
## References ##
1. [Simple implementation](https://www.tomshardware.com/how-to/python-remove-image-backgrounds)
2. [medium article](https://medium.com/axinc-ai/u2net-a-machine-learning-model-that-performs-object-cropping-in-a-single-shot-48adfc158483)
3. [Replacing backgrounds.](https://docs.openvino.ai/latest/notebooks/205-vision-background-removal-with-output.html#visualize-results)
4. [`u2net`](https://github.com/axinc-ai/ailia-models/tree/master/background_removal/u2net)
5. [`u-2-net`](https://github.com/xuebinqin/U-2-Net)
6. [`rembg`](https://github.com/danielgatis/rembg) is a `pip` installable tool.
