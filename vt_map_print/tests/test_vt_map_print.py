import unittest

from vt_map_print.printer import VT_Map_Print

class PrintTest(unittest.TestCase):

    def setUp(self):
        self.vt_map_print = VT_Map_Print()

    def test_create_vt_map_print(self):
        self.vt_map_print

    def test_return_tile_download_tuple(self):
        count = self.vt_map_print.tile_count((2637, 6378),(2641, 6380))
        self.assertTupleEqual(count, (4, 2))

    def test_returns_correct_google_tiles(self):
        tl_tile = self.vt_map_print.tile_from_lat_lon(36.985003092, -122.0581054, 14)
        br_tile = self.vt_map_print.tile_from_lat_lon(36.949891786, -121.9702148, 14)
        self.assertTrue(tl_tile[0] == 2637)
        self.assertTrue(tl_tile[1] == 6378)
        self.assertTrue(br_tile[0] == 2641)
        self.assertTrue(br_tile[1] == 6380)

    def test_returns_pixel_count_tuple(self):
        count = self.vt_map_print.pixel_count((4, 2), "@2x", 256)
        self.assertTupleEqual(count, (2048, 1024))

    # def test_validate_accept_inputs(self):
    #     parser = self.vt_map_print.parse_args([14, 36.985003092, -122.0581054, 36.949891786, -121.9702148])
    #     for item in parser:
    #         print(item)
    #     self.assertTrue(parser.zoom)
