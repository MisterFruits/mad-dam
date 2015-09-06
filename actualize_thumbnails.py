from PIL import Image
import os

SIZE = (256, 256)


def maj_thumbnail(large_dir, thumbnail_dir):
    for original_image in os.listdir(large_dir):
        im = Image.open(os.path.join(large_dir, original_image))
        im.thumbnail(SIZE, Image.ANTIALIAS)
        im.save(os.path.join(thumbnail_dir, original_image))


def main():
    pass

if __name__ == '__main__':
    main()
