import settings.pic
from PIL import Image, ImageDraw


def new_base_img(color_code):
    base_img = Image.new(settings.pic.mode, (settings.pic.size, settings.pic.size))
    draw = ImageDraw.Draw(base_img)
    draw.ellipse(
        (
            0,
            0,
            settings.pic.size,
            settings.pic.size,
        ),
        fill=color_code)
    return base_img
