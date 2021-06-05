from enum import Enum

from openpyxl import load_workbook


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
        self.city = city  # регион/город
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
    for row in list(read_file("../resorces/cities.xlsx"))[1:]:
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


def calc_width_insulation_material(i: Input):
    return 1
