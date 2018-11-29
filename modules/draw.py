from PIL import Image, ImageDraw, ImageFont
import settings.pic
import settings.fonts


def draw_element_name(element_name, img, text_color):
    font_size = int(settings.pic.size * settings.fonts.name_font_percentage)
    desc_font_size = int(settings.pic.size * settings.fonts.id_font_percentage)
    fnt = ImageFont.truetype(
        settings.fonts.name_font_dir,
        font_size
    )
    draw_pic = ImageDraw.Draw(img)
    text_w, text_h = draw_pic.textsize(element_name, font=fnt)
    draw_pic.text(
        (
            (settings.pic.size - text_w) / 2,
            (settings.pic.size - text_h) / 2 + settings.fonts.name_font_vertical_fix * font_size - (desc_font_size / 2)
        ), element_name, fill=text_color, font=fnt)
    return img


def draw_element_id(element_id, img, text_color):
    name_font_size = int(settings.pic.size * settings.fonts.name_font_percentage)
    font_size = int(settings.pic.size * settings.fonts.id_font_percentage)
    fnt = ImageFont.truetype(
        settings.fonts.id_font_dir,
        font_size
    )
    draw_pic = ImageDraw.Draw(img)
    text_w, text_h = draw_pic.textsize(element_id, font=fnt)
    draw_pic.text(
        (
            (settings.pic.size - text_w) / 2,
            ((settings.pic.size - name_font_size) / 2 - text_w) / 2,
        ), element_id, fill=text_color, font=fnt)
    return img


def draw_element_desc(element_full_name, element_mass, img, text_color):
    name_font_size = int(settings.pic.size * settings.fonts.name_font_percentage)
    font_size = int(settings.pic.size * settings.fonts.id_font_percentage)
    fnt = ImageFont.truetype(
        settings.fonts.id_font_dir,
        font_size
    )
    draw_pic = ImageDraw.Draw(img)
    text_write = element_full_name
    text_w, text_h = draw_pic.textsize(text_write, font=fnt)
    draw_pic.text(
        (
            (settings.pic.size - text_w) / 2,
            settings.pic.size - ((settings.pic.size - name_font_size) / 2) - text_h / 2,
        ), element_full_name, fill=text_color, font=fnt)
    text_w, _ = draw_pic.textsize(element_mass, font=fnt)
    draw_pic.text(
        (
            (settings.pic.size - text_w) / 2,
            settings.pic.size - ((settings.pic.size - name_font_size) / 2) + text_h / 2,
        ), element_mass, fill=text_color, font=fnt)
    return img
