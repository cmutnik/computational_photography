from PIL import Image, ImageOps

inFilename = "figs/Obs_PS_lsum_aitoff_map.png"
outFilename = "figs/out_boarder_around_image.png"

ImageOps.expand(Image.open(inFilename), border=30, fill="white").save(outFilename)
