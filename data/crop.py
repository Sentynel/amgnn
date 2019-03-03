#! /usr/bin/env python3
import os
import sys

from PIL import Image

dest = sys.argv[1]

for i in os.listdir(dest):
    im = Image.open("{}/{}".format(dest, i))
    size = min(im.width, im.height)
    left = int((im.width - size) / 2)
    top = int((im.height - size) / 2)
    im = im.crop((left, top, left+size, top+size))
    im = im.resize((150,150), Image.BICUBIC)
    im.save("{}/{}".format(dest, i))
