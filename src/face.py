from tkinter import *
from tkinter import ttk

from src.core import get_regions_list

regions = get_regions_list()


def main():
    window = Tk()
    window.title("Расчет толщины утеплителя для 3D принтера")
    window.geometry('500x500')

    combobox = ttk.Combobox(window, values=sorted(list(regions)), width=30)
    combobox.place(x=10, y=10)

    window.mainloop()


if __name__ == '__main__':
    main()
