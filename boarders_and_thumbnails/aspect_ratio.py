from PIL import Image

image  = Image.open('./poster2.png')
width, height  = image.size[0], image.size[1]

aspect = width / float(height)

ideal_width = 660
ideal_height = 1000

ideal_aspect = ideal_width / float(ideal_height)

if aspect > ideal_aspect:
    # Then crop the left and right edges:
    new_width = int(ideal_aspect * height)
    offset = (width - new_width) / 2
    resize = (offset, 0, width - offset, height)
else:
    # ... crop the top and bottom:
    new_height = int(width / ideal_aspect)
    offset = (height - new_height) / 2
    resize = (0, offset, width, height - offset)

thumb = image.crop(resize).resize((ideal_width, ideal_height), Image.ANTIALIAS)
thumb.save('poster.png')