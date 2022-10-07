from rembg import remove
from PIL import Image

if __name__ == '__main__':
    input_path = 'cl.png'
    output_path = 'output.png'
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)

