from enum import Enum

from openpyxl import load_workbook
from sympy import Symbol
from sympy.solvers import solve


# тип стены
class WallType(Enum):
    STRETCH = 1  # гибкая связь
    STRONG = 2  # жесткая связь


class Input:

    def __init__(self, city: str,
                 temperature: float,
                 humidity: float,
                 wall_type: WallType,
                 insulation_material: str,
                 width_print_layer: float,
                 width_construction_layer: float):
        self.city = city  # город
        self.temperature = temperature  # температура внутри помещения
        self.humidity = humidity  # относительная влажность внутри помещения
        self.wall_type = wall_type  # тип стены
        self.insulation_material = insulation_material  # утеплитель
        self.width_print_layer = width_print_layer  # толщина печатаемого слоя
        self.width_construction_layer = width_construction_layer  # толщина конструктивного слоя


def read_file(file_path: str) -> list:
    wb = load_workbook(file_path, data_only=True)
    sheet = wb.get_sheet_by_name(wb.sheetnames[0])
    rows = sheet.rows
    wb.close()
    return rows


def get_regions_list():
    regions = {}
    cities = {}
    for row in list(read_file("resources/cities.xlsx"))[1:]:
        region = row[0].value
        city = row[1].value
        count_days = row[2].value
        temperature = row[3].value
        if region not in regions:
            regions[region] = {"cities": []}
        c = {"city": city,
             "count_days": count_days,
             "temperature": temperature}
        regions[region]["cities"].append(c)
        cities[city] = c
    return regions, cities


def get_materials_list():
    materials = {}
    for row in list(read_file("resources/material.xlsx"))[1:]:
        material = row[0].value
        coefficient = row[1].value
        materials[material] = coefficient
    return materials


def mm2m(mm):
    return mm / 1000


def calc_layers(i: Input):
    l7 = 0
    if i.wall_type == WallType.STRONG:
        l7 = i.width_print_layer
    l5 = i.width_construction_layer
    return mm2m(4 * i.width_print_layer + l5 + l7) / 1.5


def calc_width_insulation_material(i: Input):
    c = cities[i.city]
    temperature_out = c['temperature']
    count_days = c['count_days']
    lambda2 = materials[i.insulation_material]

    gcop = (i.temperature - temperature_out) * count_days
    a = 0.00035
    b = 1.4
    r = a * gcop + b

    x = Symbol('x')
    res = solve(1 / 8.7 + calc_layers(i) + mm2m(x) / lambda2 + 1 / 23 - r, x)
    return res[0]


regions, cities = get_regions_list()
materials = get_materials_list()
