#!/bin/bash

# ONLY loop through ODD numbers and lead with 0s if needed
for i in $(seq -w 01 02 101); do
   scp ab100.jpg $i.jpg
done

# ONLY loop through EVEN numbers and lead with 0s if needed
for i in $(seq -w 02 02 100); do
   scp ba100.jpg $i.jpg
done

