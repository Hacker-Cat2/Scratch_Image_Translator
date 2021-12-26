import colorsys
from PIL import Image


def add_zeros(value: str = '', length: int = 1) -> str:
    return ('0' * (length - len(value))) + str(value)


def convert(image_path: str = '') -> tuple[bool, str]:
    max_pixels = 2**32
    image_code = ''
    try:
        image = Image.open(image_path)
    except Exception as exception:
        return False, f"Error: {exception}"
    if image.size[0] * image.size[1] > max_pixels:
        return False, "Error: Image is too large"
    image_code = f'{image.size[0]},{image.size[1]},'
    pixels = image.load()
    for y in range(0, image.size[1]):
        temp = ''
        for x in range(0, image.size[0]):
            pixel = pixels[x, y]
            if len(pixel) > 3:
                a = pixel[3]
            else:
                a = 255.0
            h, s, v = colorsys.rgb_to_hsv(pixel[0] / 255, pixel[1] / 255, pixel[2] / 255)
            temp += add_zeros(str(round(h * 100)), 3) + add_zeros(str(round(s * 100)), 3) + add_zeros(str(round(v * 100)), 3) + add_zeros(str(100 - round(a / 2.55)), 3)
        image_code += temp
        print(str(round((y + 1) / image.size[1] * 10000) / 100) + '%', end='\r')
    print()
    return True, image_code
