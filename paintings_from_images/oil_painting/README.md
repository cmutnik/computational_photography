# Oil Paintings #
A more detailed description of the underlying code can be found [here.](https://github.com/ctmakro/opencv_playground)

----
## Usage ##
1. ```sh
    ipython -i painterfun.py
    ```

2. ```ipy
    load("./other_image.jpg")
    r(10) # select a number that works best
    r(2) # consecutive strokes can be added
    img = repaint(upscale=1)
    cv2.imwrite("./other_image_oilpainted.jpg", img)
    ```

----
## Example ##
<img src="../../figs/zoom_virtual_backgrounds/flower.jpg" width="40%"> <img src="../../figs/paintings/flower_oilpainted.jpg" width="40%">