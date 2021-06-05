import unittest

from src.core import calc_width_insulation_material, Input, WallType

data = [
    {"waiting": 159.6,
     "in": Input("Барнаул", 21, 0, WallType.STRETCH, "Полистиролбетон (плотность 200 кг/м3)", 60, 240)},
]


class TestCore(unittest.TestCase):

    def test_table(self):
        for d in data:
            w = calc_width_insulation_material(d["in"])
            self.assertEqual(w, d["waiting"])
