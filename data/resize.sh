#! /bin/bash
if [ -z "$1" ]
then
    echo "usage: ./resize.sh folder/"
    exit 1
fi

for i in $1/*
do
    convert $i -resize 150x150 $i
done
