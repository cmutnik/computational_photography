
# %%
import sys
import cv2
import numpy as np

# dir = sys.path[0]
path_to_file = "../icon_ideas/octopus-icon-logo-vector-illustration-design-template_598213-1260-removebg-preview.png"
# path_to_file = "../icon_ideas/octopus-icon-logo-vector-illustration-design-template_598213-1260.jpeg"

im = cv2.imread(path_to_file, -1)

# Fill anywhere not fully transparent.
im[np.where(im[:, :, 3] != 0)] = (0, 0, 0, 255)

cv2.imwrite('000_im_.png', im)


# %%
from PIL import Image

in_path = "../icon_ideas/octopus-icon-vector-33558706.png"
out_path = "000_img2.png"

img = Image.open(in_path)
img = img.convert("RGBA")

imgnp = np.array(img)

white = np.sum(imgnp[:,:,:3], axis=2)
white_mask = np.where(white == 255*3, 1, 0)

alpha = np.where(white_mask, 0, imgnp[:,:,-1])

imgnp[:,:,-1] = alpha 

img = Image.fromarray(np.uint8(imgnp))
img.save(out_path, "PNG")

# %%
