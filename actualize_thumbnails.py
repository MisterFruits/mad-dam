#!/usr/bin/env python
# coding: utf-8

from PIL import Image
import os
import argparse

DEFAULT_SIZE = (256, 256)


def maj_thumbnail(large_dir, thumbnail_dir):
    for original_image in os.listdir(large_dir):
        im = Image.open(os.path.join(large_dir, original_image))
        im.thumbnail(DEFAULT_SIZE, Image.ANTIALIAS)
        im.save(os.path.join(thumbnail_dir, original_image))


def main():
    parser = argparse.ArgumentParser(description='''Makes thumbnails\
of a bunch of images''')
    parser.add_argument("idir")
    parser.add_argument("odir")

    args = parser.parse_args()
    maj_thumbnail(args.idir, args.odir)

if __name__ == '__main__':
    main()
