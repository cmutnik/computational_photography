#!/bin/bash
#
## Shell script to extract frames from a video and save them as images
#

## TODO: make optional command line arg for output name/filepath

#eval $@

if [ "$#" -lt 1 ] || [ "$#" -gt 2 ]; then
    echo "Usage: ./extract_video_frames.sh <videoFilename.mp4>"
    #return;
    exit 0;
fi

## Cast first commandline argument as input filename
_filename_=$1

function ceiling_value()
{
    echo "7.2" | perl -nl -MPOSIX -e 'print ceil($_);'
}

function getFPS()   ## get input frame-rate (fps) 
{
    local func_result=$(ffmpeg -i ${_filename_} 2>&1 | sed -n "s/.*, \(.*\) fp.*/\1/p")
    #echo "$func_result"

    ## ceiling value to account for fractional fps
    echo "$func_result" | perl -nl -MPOSIX -e 'print ceil($_);'
}


function convert_video_to_still_frames()   ## extract each frame of a video to an image
{
    ## TODO: make optional command line arg for output name/filepath
    ffmpeg -i ${_filename_} -vf fps="$(getFPS)" out%d.png
}

## Call function to run code
convert_video_to_still_frames

exit 0




