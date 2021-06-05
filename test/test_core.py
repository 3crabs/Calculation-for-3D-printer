import unittest

from src.core import calc_width_insulation_material, Input, WallType

data = [
    {"waiting": 159,
     "in": Input("Барнаул", 21, 0, WallType.STRETCH, "Полистиролбетон (плотность 200 кг/м3)", 60, 240)},
    {"waiting": 97,
     "in": Input("Липецк", 22, 0, WallType.STRETCH, "Минеральная вата (плотность 30 кг/м3)", 40, 250)},
    {"waiting": 71,
     "in": Input("Белгород", 20, 0, WallType.STRONG, "Пенополистирол (плотность 30 кг/м3)", 80, 200)},
    {"waiting": 29,
     "in": Input("Сочи", 22, 0, WallType.STRONG, "Пенополиуретан (плотность 30 кг/м3)", 50, 200)},
    {"waiting": 76,
     "in": Input("Москва", 21, 0, WallType.STRETCH, "Стекловата (плотность 200 кг/м3)", 80, 220)},
]


class TestCore(unittest.TestCase):

    def test_table(self):
        for d in data:
            w = calc_width_insulation_material(d["in"])
            print(d["waiting"], '~=', round(w), '(' + str(w) + ')')
            self.assertTrue(abs(w - d["waiting"]) < 1)
