#!/bin/bash

_MAX_VAL=300

###########################################################################
# now made ab100 by reversing order
#   b.jpg even numbers
#   a.jpg odd numbers
cd infiles/
rm ./*.jpg
scp ../a.jpg .
scp ../b.jpg .

# ONLY loop through ODD numbers and lead with 0s if needed
for i in $(seq -w 01 02 $_MAX_VAL); do
   scp a.jpg $i.jpg
done

# ONLY loop through EVEN numbers and lead with 0s if needed
for i in $(seq -w 02 02 $_MAX_VAL); do
   scp b.jpg $i.jpg
done

rm a.jpg
rm b.jpg
echo "MADE infiles/* for ab100_runall.jpg"

cd -

python vertical.py

mv outfiles/* ab100_runall.jpg

echo "FINISHED ab100_runall.jpg"


###########################################################################
# now made ba100 by reversing order
#   a.jpg even numbers
#   b.jpg odd numbers

cd infiles/
rm ./*.jpg
scp ../a.jpg .
scp ../b.jpg .

# ONLY loop through ODD numbers and lead with 0s if needed
for i in $(seq -w 01 02 $_MAX_VAL); do
   scp b.jpg $i.jpg
done

# ONLY loop through EVEN numbers and lead with 0s if needed
for i in $(seq -w 02 02 $_MAX_VAL); do
   scp a.jpg $i.jpg
done

rm a.jpg
rm b.jpg
echo "MADE infiles/* for ba100_runall.jpg"

cd -

python vertical.py

mv outfiles/* ba100_runall.jpg

echo "FINISHED ba100_runall.jpg"



###########################################################################
# stitch them together

cd infiles/
rm ./*.jpg
scp ../ab100_runall.jpg .
scp ../ba100_runall.jpg .


for i in $(seq -w 01 02 $_MAX_VAL); do
   scp ab100_runall.jpg $i.jpg
done

# ONLY loop through EVEN numbers and lead with 0s if needed
for i in $(seq -w 02 02 $_MAX_VAL); do
   scp ba100_runall.jpg $i.jpg
done

rm ab100_runall.jpg
rm ba100_runall.jpg
echo "MADE infiles/* for ab100_ba100_runall.jpg"

cd -
python horizontal.py

mv outfiles/* ab100_ba100_runall.jpg

echo "FINISHED ab100_ba100_runall.jpg"

rm infiles/*.jpg