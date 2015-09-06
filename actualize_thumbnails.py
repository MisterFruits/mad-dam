#!/usr/bin/env python
# coding: utf-8

from PIL import Image
import os
import argparse

DEFAULT_SIZE = (256, 256)
DEFAULT_EXTS = ('.jpg', '.png', '.bmp', '.tiff')


def maj_thumbnails(idir, odir, size=DEFAULT_SIZE, force=False):
    for img, name in iterimages(idir):
        if os.path.exists(os.path.join(odir, name)) and not force:
            continue
        img.thumbnail(size, Image.ANTIALIAS)
        img.save(os.path.join(odir, name))


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
