#https://bespokeblog.wordpress.com/category/programming/python/
import sys
from PIL import Image
import glob

# REPLACE "im1.jpg" with imgList[0]
# REPLACE imdir+'im%d.jpg'%(imnum) with imgList values
'''
imgList = glob.glob('./*.JPG')

first = True
for i in imgList:
    temp = np.array(Image.open(i))
'''

def imageblend(imdir, numimages, blendwidth=0):
    if not blendwidth%2 == 0:
        raise Exception('blendwidth not even')
 
    im = Image.open(imdir+"im1.jpg")
    (width, height) = im.size
 
    for i in range(1, numimages):
        imnum = i+1
        centre = i*width/numimages - 1
 
        im_i = Image.open(imdir+'im%d.jpg'%(imnum))
 
        for x in range(blendwidth):
            col_ind = centre - (blendwidth/2) + x +1
            col_box = (col_ind, 0, col_ind+1, height-1)
            col_o = im.copy().crop(col_box)
            col_i = im_i.copy().crop(col_box)
            col = Image.blend(col_o, col_i, float(x)/blendwidth)
            im.paste(col, col_box)
 
        rest_box = (centre+blendwidth/2+1, 0, width-1, height-1)
        rest = im_i.copy().crop(rest_box)
        im.paste(rest, rest_box)
 
    im.save(imdir+"im_output.jpg")
 
def main():
    # conditional that sets deafaults incase args arent provided
    '''
    if len(sys.argv) < 4:
        imdir = './'
        ext = 'JPG'
        numimages = 54
        print 'Proper use:\n$python mod_mergeimages_160929.py [/path/to/imgs/] [img_extention] [#_of_imgs]'
        #print 'Directory and extention not specified - defaults used'
    else:
        imdir = sys.argv[1]
        ext = sys.argv[2]
        numimages = sys.argv[3]
        #numimages = len(glob.glob('./*.' + ext))
    '''
    if len(sys.argv) < 3:
        imdir = './'
        ext = 'JPG'
        print 'Proper use:\n$python mod_mergeimages_160929.py [/path/to/imgs/] [img_extention]'
        #print 'Directory and extention not specified - defaults used'
    else:
        imdir = sys.argv[1]
        ext = sys.argv[2]

    # number of images in specified dir, with specified extention
    numimages = len(glob.glob(imdir + '*.' + ext))
    print numimages
    #imgList = glob.glob('./*.' + ext)

    imageblend(imdir, numimages)
 
if __name__=='__main__':
    main()