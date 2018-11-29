import csv
import settings.fonts


def find_color_code(element_id):
    colors_csv = open('colors.csv', newline='')
    colors_reader = csv.reader(colors_csv, delimiter=',', quotechar='"')
    for i, row in enumerate(colors_reader):
        if i == int(element_id):
            return "#" + row[3]


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def find_couple_color(origin_color):
    rgb = hex_to_rgb(origin_color)
    o = round(((int(rgb[0]) * 299) +
               (int(rgb[1]) * 587) +
               (int(rgb[2]) * 114)) / 1000)
    if o > settings.fonts.dark_value:
        return settings.fonts.dark_color
    else:
        return settings.fonts.bright_color
