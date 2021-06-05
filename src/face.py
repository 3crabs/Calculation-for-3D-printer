from tkinter import *
from tkinter import ttk

from src.core import regions, materials

window = Tk()
regions_combobox = ttk.Combobox(window, values=sorted(list(regions)), width=30, state='readonly')
city_combobox = ttk.Combobox(window, values=sorted(list(regions)), width=30, state='readonly')
materials_combobox = ttk.Combobox(window, values=sorted(list(materials)), width=40, state='readonly')


def hi(arg):
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
    window.geometry('500x500')

    regions_combobox.place(x=10, y=10)
    regions_combobox.bind("<<ComboboxSelected>>", hi)

    city_combobox.place(x=10, y=40)
    city_combobox["state"] = DISABLED

    materials_combobox.place(x=10, y=70)

    window.mainloop()


if __name__ == '__main__':
    main()
