import unittest

from src.core import calc_width_insulation_material

data = [
    {"waiting": 1, "in": {}},
]


class TestCore(unittest.TestCase):

    def test_table(self):
        for d in data:
            w = calc_width_insulation_material(d["in"])
            self.assertEqual(w, d["waiting"])
