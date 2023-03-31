import os
from PIL import Image, ImageDraw, ImageFont


def calculate_font_size(width, height):
    x, y = int(width / 2), int(height / 2)
    if y > x:
        return int(y / 6)
    else:
        return int(x / 6)


def watermark_image(image_url, watermark_text):
    if os.name == 'nt':
        image_url = image_url.replace('\\', '/')

    image = Image.open(image_url)
    width, height = image.size

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("arial.ttf", calculate_font_size(width, height))

    draw.text((int(width / 2), int(height / 2)), watermark_text, fill=(0, 0, 0), font=font, anchor='ms')

    image.save('watermarked.jpg')
