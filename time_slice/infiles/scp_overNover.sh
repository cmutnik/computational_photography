#!/bin/bash

# ONLY loop through ODD numbers and lead with 0s if needed
for i in $(seq -w 01 02 5480); do
   scp DB9A2216.JPG $i.jpg
done

# ONLY loop through EVEN numbers and lead with 0s if needed
for i in $(seq -w 02 02 5479); do
   scp DB9A2069.JPG $i.jpg
done

