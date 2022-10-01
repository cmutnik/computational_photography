#!/usr/bin/python

import os
import string
import time
import shutil

#Here's the Python code for unloading the camera. It recurses through SRCDIR and names each image with the date & time before copying the images to DESTDIR.

###################################################
__SRCDIR__ = "/mnt/camera"
__DESTDIR__ = "/home/pictures/recent"
###################################################
def cbwalk(arg, dirname, names):
    sdatetime = time.strftime("%y%m%d%H%M")
    for name in names:
    	if string.lower(name[-3:]) in ("jpg", "mov"):
    		srcfile = "%s/%s" % (dirname, name)
    		destfile = "%s/%s_%s" % (__DESTDIR__, sdatetime, name)
                	print destfile
    		shutil.copyfile( srcfile, destfile)
###################################################
if __name__ == "__main__":
    os.path.walk(__SRCDIR__, cbwalk, None)