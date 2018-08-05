import sys
from pprint import pprint

from vt_map_print import VT_Map_Print
from vt_map_print.positive_affirmations.p_a import *
from vt_map_print import config


def get_tile_info():
    printer = VT_Map_Print()
    printer.get_tile_info(sys.argv[2:])


def vt_print():
    printer = VT_Map_Print()
    printer.run_vt_map_print(sys.argv[2:])


#python like switch statement
options = {"python_test" : print_affirmation,
            "vt_print" : vt_print,
            "get_tile_info" : get_tile_info,
}

if __name__ == '__main__':
    options[sys.argv[1]]()
