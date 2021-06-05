from enum import Enum


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


def calc_width_insulation_material(i: Input):
    return 1
