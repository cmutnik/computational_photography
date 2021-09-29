# Image Boarders and Thumbnails

This started when my github profile image was the wrong size/aspect-ratio.  To fix this, I had to create a thumbnail of the [original image.](../figs/boarders_and_thumbnails/Obs_PS_lsum_aitoff_map.png).  I no longer had the data to re-plot with a new figure size, so I had to work with the saved fig.

----
### Thumbnail
Compressing the image to a [thumbnail](./image2thumbnail.py) 
either ruined the aspect ratio or didn't solve the issue. 
```py
from PIL import Image

inFilename = '../figs/boarders_and_thumbnails/Obs_PS_lsum_aitoff_map.png'
outFilename = '../figs/boarders_and_thumbnails/out_img2thumbnail.png'

img = Image.open(inFilename)
img.thumbnail([500, 500],Image.ANTIALIAS)
img.save(outFilename) 
```

----
### Boarder
Instead of making a thumbnail, I decided to add a boarder to the existing image.  [`addBackground.py`](./addBackground.py) makes a background and pastes the image on top of the backgroud.
```py
from PIL import Image

inFilename = '../figs/boarders_and_thumbnails/Obs_PS_lsum_aitoff_map.png'
outFilename = '../figs/boarders_and_thumbnails/out_addBackground.jpg'

img = Image.open(inFilename)
x1, y1, x2, y2 = -10, -20, 1000, 1000  # cropping coordinates
im = Image.new('RGB', (x2 - x1, y2 - y1), (255, 255, 255))
im.paste(img, (-x1, -y1))
im.save(outFilename)
```

This works fine, but you have to choose the placement of overlaid image.  Instead, I found the best way was to simply add a boarder around the original image, shown in [`boarder_around_image.py`:](./boarder_around_image.py)
```py
from PIL import Image, ImageOps

inFilename = '../figs/boarders_and_thumbnails/Obs_PS_lsum_aitoff_map.png'
outFilename = '../figs/boarders_and_thumbnails/out_boarder_around_image.png'

ImageOps.expand(Image.open(inFilename),border=30,fill='white').save(outFilename)
```