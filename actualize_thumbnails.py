#!/usr/bin/env python
# coding: utf-8

from PIL import Image
import os
import argparse

DEFAULT_SIZE = (256, 256)


def maj_thumbnails(large_dir, thumbnail_dir, size=DEFAULT_SIZE):
    for img, name in iterimages(large_dir):
        img.thumbnail(DEFAULT_SIZE, Image.ANTIALIAS)
        img.save(os.path.join(thumbnail_dir, name))


def iterimages(idir, ext=('.jpg', '.png', '.bmp')):
    for image in os.listdiar(idir):
        if os.path.splitext(image) in ext:
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
