#!/usr/bin/env python
# coding: utf-8

from PIL import Image
import os
import argparse
import logging

DEFAULT_SIZE = 256
DEFAULT_EXTS = ('.jpg', '.png', '.bmp', '.tiff')

THUMBNAIL_PATH_EXIST_WARNING = 'The file "{}" exists and wont be overwritten,\
use "--force" option to force overwritting'


def maj_thumbnails(idir, odir, size=DEFAULT_SIZE, force=False):
    for img, name in iterimages(idir):
        thumb_path = os.path.join(odir, name)
        if os.path.exists(thumb_path) and not force:
            logging.warning(THUMBNAIL_PATH_EXIST_WARNING.format(thumb_path))
            continue
        img.thumbnail((size, size), Image.ANTIALIAS)
        img.save(thumb_path)


def iterimages(idir, exts=DEFAULT_EXTS):
    for image in os.listdir(idir):
        _, ext = os.path.splitext(image)
        if ext in exts:
            yield Image.open(os.path.join(idir, image)), image


def main():
    parser = argparse.ArgumentParser(description='''Makes thumbnails\
of a bunch of images''')
    parser.add_argument("idir", help='image source directory')
    parser.add_argument("odir", help='thumbnail target directory')
    parser.add_argument("-f", "--force",
                        action='store_true',
                        help='overwritte generated file if exists')
    parser.add_argument('-s', '--size',
                        type=int,
                        default=DEFAULT_SIZE,
                        help='generated thumbnail size')

    args = parser.parse_args()
    maj_thumbnails(args.idir, args.odir, args.size, args.force)

if __name__ == '__main__':
    main()
