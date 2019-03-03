#! /bin/bash
if [ -z "$1" ]
then
    echo "usage: ./convert.sh folder/"
    exit 1
fi

for i in $1/*.png
do
    convert $i ${i%.png}.jpg
done
