# Oil Paintings #
A more detailed description of the underlying code can be found [here.](https://github.com/ctmakro/opencv_playground)

----
## Usage ##
1. ```sh
    ipython -i painterfun.py
    ```

2. ```ipy
    load('image.jpg')
    r(10) # select a number that works best
    r(2) # consecutive strokes can be added
    img = repaint(upscale=1)
    cv2.imwrite('abc.png',img)
    ```

----
## Example ##
<img src="../../figs/paintings/IMG_3477_1.jpg" width="40%"> <img src="../../figs/paintings/IMG_3477_1_oil.jpg" width="40%">