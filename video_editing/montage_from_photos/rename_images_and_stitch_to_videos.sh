#!/bin/bash
<<EOF
#ffmpeg -f image2 -r 4 -i ./outDubs1/img%03d.jpg -loop -1 out.gif

# line above does NOT work, it stops after a certain number of frames
# ffmpeg -f image2 -i ./outDubs1/img%03d.jpg -loop -1 out1.gif
ffmpeg -f image2 -i ./6/G038845%01d.JPG -loop -1 out.gif

ffmpeg -f image2 -i ./testall/*/G0%06d.JPG -loop -1 out2.gif

# re-number all files in a dir using a loop with: mv [file list] [number sequence]
# OR
# cat a list of all files in dir and loop through list
EOF

function rename_files(){	# rename images to fit desired convention
    file_list=$(ls ./testall/*.JPG)
    i=0
    for img in $file_list; do 
        base_path=$(echo $img | awk -F'G0' '{print $1}' -)
        i=$((i+1))
        
        if [[ $i -lt 10 ]]; then 
            newname=${base_path}img00${i}.JPG
        elif [[ $i -lt 100 ]]; then
            newname=${base_path}img0${i}.JPG
        else
            newname=${base_path}img${i}.JPG
        fi
        
        mv $img $newname
    done
}

function make_animation(){
    # ffmpeg -f image2 -i ./testall/img%03d.JPG -loop -1 out1.gif -y
    ffmpeg -f image2 -r 4 -i ./testall/img%03d.jpg -c:v libx264 -pix_fmt yuv420p out3.mp4 -y
    # ffmpeg -f image2 -i ./testall/img%03d.jpg -c:v libx264 -pix_fmt yuv420p -r 2 out6.mp4 -y
}

if [ 'img001.JPG' != $(ls -U ./testall/ | head -1) ]; then rename_files; fi
make_animation
