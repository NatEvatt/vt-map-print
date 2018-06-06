import unittest

from vt_map_print.printer import VT_Map_Print

class PrintTest(unittest.TestCase):

    def setUp(self):
        self.vt_map_print = VT_Map_Print()

    # def test_create_vt_map_print(self):
    #     self.vt_map_print

    def test_validate_accept_inputs(self):
        parser = self.vt_map_print.parse_args([14, 36.985003092, -122.0581054, 36.949891786, -121.9702148])
        for item in parser:
            print(item)
        self.assertTrue(parser.zoom)
