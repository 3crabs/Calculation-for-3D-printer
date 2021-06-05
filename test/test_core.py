import unittest

from src.core import calc_width_insulation_material, Input

data = [
    {"waiting": 1, "in": Input()},
]


class TestCore(unittest.TestCase):

    def test_table(self):
        for d in data:
            w = calc_width_insulation_material(d["in"])
            self.assertEqual(w, d["waiting"])
