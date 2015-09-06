#!/usr/bin/env python
# coding: utf-8

from PIL import Image
import os
import argparse

DEFAULT_SIZE = (256, 256)
DEFAULT_EXTS = ('.jpg', '.png', '.bmp')


def maj_thumbnails(large_dir, thumbnail_dir, size=DEFAULT_SIZE):
    for img, name in iterimages(large_dir):
        img.thumbnail(size, Image.ANTIALIAS)
        img.save(os.path.join(thumbnail_dir, name))


def iterimages(idir, exts=DEFAULT_EXTS):
    for image in os.listdir(idir):
        _, ext = os.path.splitext(image)
        if ext in exts:
            yield Image.open(os.path.join(idir, image)), image


def main():
    parser = argparse.ArgumentParser(description='''Makes thumbnails\
of a bunch of images''')
    parser.add_argument("idir")
    parser.add_argument("odir")

    args = parser.parse_args()
    maj_thumbnails(args.idir, args.odir)

if __name__ == '__main__':
    main()
