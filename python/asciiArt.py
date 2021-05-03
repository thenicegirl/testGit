from PIL import Image, ImageFont
import numpy as np


def ascii_art(file):
    im = Image.open(file)

    # convert to gray scale image
    im = im.convert('L')

    sample_rate = 0.05

    # Compute letter aspect ratio
    # new_im_size = [int(x * sample_rate) for x in im.size]
    font = ImageFont.truetype('SourceCodePro-Regular.ttf')
    aspect_ratio = font.getsize('x')[0] / font.getsize('x')[1]
    new_im_size = np.array(
        [im.size[0] * sample_rate, im.size[1] * sample_rate * aspect_ratio]
    ).astype(int)

    # Downsample the image
    im = im.resize(new_im_size)

    # Convert to numpy array for image manipulation
    im = np.array(im)

    # Define all the symbols in ascending order that will form the final ascii
    symbols = np.array(list('.-vM'))

    # Normalize minimum and maximum to [0, max_symbol_index)
    im = (im - im.min()) / (im.max() - im.min()) * (symbols.size - 1)

    # Generate the ascii art
    ascii = symbols[im.astype(int)]
    lines = '\n'.join((''.join(r) for r in ascii))
    print(lines)


if __name__ == '__main__':
    ascii_art('./neko.jpg')
