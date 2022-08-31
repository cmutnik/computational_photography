# Generative Adversarial Network (GAN) #
Use GANs to convert images to anime style animations.  The models currently implemented here were trained on, and therefore work best on, images of human faces.

The following notebooks is from [here.](https://github.com/bryandlee/animegan2-pytorch)  
[face_to_Anime_with_AnimeGANv2.ipynb](./notebooks/face_to_Anime_with_AnimeGANv2.ipynb) shows how a pre-trained GAN can be applied to desired images.  This notebook was run in colab with the files designated locally.  Smaller image files stored remotely can be used by changing by altering the local filenames:
```py
# designate filenames for locally saved copies
img_path_name = "/content/GC6A5200.JPG"
three_images = "/content/GC6A5474_lowres.jpg"
```
to become references for how to store the remote files locally:
```py
from urllib.request import urlretrieve

# save remote the image to our local storage
urlretrieve("https://pbs.twimg.com/profile_images/691700243809718272/z7XZUARB_400x400.jpg", img_path_name)
torch.hub.download_url_to_file("https://www.cnet.com/a/img/LxPnVvP4ONxWlQmXOI4j-9m6d90=/940x0/2019/03/27/c36a11ff-4029-4eb2-8ca9-72143ea8e596/screen-shot-2019-03-27-at-11-51-29-am.png", three_images)
```