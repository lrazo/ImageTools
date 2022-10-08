
from rembg import remove
from PIL import Image


def remove_background(input_path='cl.png', output_path='output.png'):
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)


def mirror(input_path='cl.png', output_path='mirror.png'):
    img = Image.open(input_path)
    mirror_image = img.transpose(Image.FLIP_LEFT_RIGHT)
    mirror_image.save(output_path)


if __name__ == '__main__':
    remove_background()
    mirror()
