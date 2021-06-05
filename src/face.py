from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

from src.core import regions, materials, WallType

window = Tk()
first_data_group = LabelFrame(window, text='Параметры среды')

regions_label = ttk.Label(first_data_group, width=30, text='Регион')
regions_combobox = ttk.Combobox(first_data_group, values=sorted(list(regions)), width=30, state='readonly')

city_label = ttk.Label(first_data_group, width=30, text='Город')
city_combobox = ttk.Combobox(first_data_group, values=sorted(list(regions)), width=30, state='readonly')

temperature_str = StringVar()
temperature_label = ttk.Label(first_data_group, width=30, text='Температура внутри помещения')
temperature_input = Entry(first_data_group, textvariable=temperature_str, width=15)
temperature_unit_label = ttk.Label(first_data_group, width=3, text='°C')

humidity_str = StringVar()
humidity_label = ttk.Label(first_data_group, width=30, text='Относительная влажность внутри помещения')
humidity_input = Entry(first_data_group, textvariable=humidity_str, width=15)
humidity_unit_label = ttk.Label(first_data_group, width=3, text='%')

second_data_group = LabelFrame(window, text='Параметры стены', height=130)

wall_type = IntVar()
wall_type.set(WallType.STRETCH)
checkbutton_left = Radiobutton(second_data_group, text="На гибких связях", value=WallType.STRETCH, variable=wall_type)
checkbutton_right = Radiobutton(second_data_group, text="На жестких связях", value=WallType.STRONG, variable=wall_type)

materials_combobox = ttk.Combobox(second_data_group, values=sorted(list(materials)), width=40, state='readonly')
material_label = ttk.Label(second_data_group, width=30, text='Утеплитель')

width_print_layer_str = StringVar()
width_print_layer_label = ttk.Label(second_data_group, width=30, text='Толщина печатаемого слоя')
width_print_layer_input = Entry(second_data_group, textvariable=width_print_layer_str, width=15)
width_print_layer_unit_label = ttk.Label(second_data_group, width=3, text='мм')

width_construction_layer_str = StringVar()
width_construction_layer_label = ttk.Label(second_data_group, width=30, text='Толщина конструктивного слоя')
width_construction_layer_input = Entry(second_data_group, textvariable=width_construction_layer_str, width=15)
width_construction_layer_unit_label = ttk.Label(second_data_group, width=3, text='мм')


def region_combobox_selector(arg):
    cities = regions[regions_combobox.get()]['cities']
    c = []
    for city in cities:
        c.append(city['city'])
    city_combobox['values'] = c
    city_combobox.set('')
    city_combobox["state"] = 'readonly'


def main():
    global window, regions_combobox, city_combobox, materials_combobox
    window.title("Расчет толщины утеплителя для 3D принтера")
    window.geometry('500x600')

    first_data_group.pack(padx=5, pady=5, expand='yes', fill='both')

    second_data_group.pack(padx=5, pady=5, expand='yes', fill='both')

    run_button = Button(window, text='Расчитать толщину утеплителя')
    run_button.pack(padx=5, pady=5, fill='both')

    answer_label = Label(window, text='Тут будет ответ')
    answer_label.pack(padx=5, pady=5, fill='both')

    regions_label.place(x=10, y=10)
    regions_combobox.place(x=270, y=10)
    regions_combobox.bind("<<ComboboxSelected>>", region_combobox_selector)

    city_label.place(x=10, y=40)
    city_combobox.place(x=270, y=40)
    city_combobox["state"] = DISABLED

    temperature_label.place(x=10, y=70)
    temperature_input.place(x=350, y=70)
    temperature_unit_label.place(x=450, y=70)

    humidity_label.place(x=10, y=100)
    humidity_input.place(x=350, y=100)
    humidity_unit_label.place(x=450, y=100)

    # Добавим изображение
    load = Image.open("../resources/stretch.png")
    load = load.resize((230, 135), Image.ADAPTIVE)
    render = ImageTk.PhotoImage(load)
    img = Label(second_data_group, image=render)
    img.image = render
    img.place(x=0, y=0)

    load = Image.open("../resources/strong.png")
    load = load.resize((230, 135), Image.ADAPTIVE)
    render = ImageTk.PhotoImage(load)
    img = Label(second_data_group, image=render)
    img.image = render
    img.place(x=245, y=0)

    checkbutton_left.place(x=60, y=140)

    checkbutton_right.place(x=300, y=140)

    material_label.place(x=10, y=180)
    materials_combobox.place(x=210, y=180)

    width_print_layer_label.place(x=10, y=210)
    width_print_layer_input.place(x=350, y=210)
    width_print_layer_unit_label.place(x=450, y=210)

    width_construction_layer_label.place(x=10, y=240)
    width_construction_layer_input.place(x=350, y=240)
    width_construction_layer_unit_label.place(x=450, y=240)

    window.mainloop()


if __name__ == '__main__':
    main()
