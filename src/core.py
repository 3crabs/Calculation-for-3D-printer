from enum import Enum

from openpyxl import load_workbook

from sympy.solvers import solve
from sympy import Symbol


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
    for row in list(read_file("../resources/cities.xlsx"))[1:]:
        region = row[0].value
        city = row[1].value
        count_days = row[2].value
        temperature = row[3].value
        if region not in regions:
            regions[region] = {"cities": []}
        regions[region]["cities"].append({"city": city,
                                          "count_days": count_days,
                                          "temperature": temperature})
    return regions


def get_materials_list():
    materials = {}
    for row in list(read_file("../resources/material.xlsx"))[1:]:
        material = row[0].value
        coefficient = row[1].value
        materials[material] = coefficient
    print(materials)
    return materials


def calc_width_insulation_material(i: Input):
    x = Symbol('x')

    a = 0.00035
    b = 1.4
    temperature_out = -7.5
    count_days = 214
    GCOP = (i.temperature - temperature_out) * count_days
    R = a * GCOP + b

    res = float()
    lambda1 = 1.5
    L1 = i.width_print_layer  # L1 = L3 = L5
    L4 = i.width_construction_layer

    lambda2 = 0.052

    if i.wall_type == WallType.STRONG:
        res = solve(1/8.7 + L1/lambda1 + x/lambda2 + L1/lambda1 + L4/lambda1, L1/lambda1 + 1/23 - R)
    if i.wall_type == WallType.STRETCH:
        res = solve(1/8.7 + L1/lambda1 + x / lambda2 + L4/lambda1, L1/lambda1 + 1/23 - R)
    print(res)
    return 1
