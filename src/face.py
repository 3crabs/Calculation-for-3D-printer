from tkinter import *
from tkinter import ttk

from src.core import get_regions_list, get_materials_list

regions = get_regions_list()
materials = get_materials_list()


def main():
    window = Tk()
    window.title("Расчет толщины утеплителя для 3D принтера")
    window.geometry('500x500')

    regions_combobox = ttk.Combobox(window, values=sorted(list(regions)), width=30)
    regions_combobox.place(x=10, y=10)

    materials_combobox = ttk.Combobox(window, values=sorted(list(materials)), width=40)
    materials_combobox.place(x=10, y=40)

    window.mainloop()


if __name__ == '__main__':
    main()
