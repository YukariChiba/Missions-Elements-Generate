import csv
import modules.image_creation
import modules.color
import modules.draw

if __name__ == '__main__':
    elements_csv = open('elements.csv', newline='')
    reader = csv.DictReader(elements_csv, delimiter=',', quotechar='"')
    for row in reader:
        base_color = modules.color.find_color_code(row['No'])
        base = modules.image_creation.new_base_img(base_color)
        couple_color = modules.color.find_couple_color(base_color)
        draw = modules.draw.draw_element_name(row['Sym.'], base, couple_color)
        draw = modules.draw.draw_element_id(row['No'], draw, couple_color)
        draw = modules.draw.draw_element_desc(row['Name'], row['AtomicWeight'], draw, couple_color)
        # draw.show()
        draw.save("results/" + row['No'] + ".png")
