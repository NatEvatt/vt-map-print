import sys
from pprint import pprint

from vt_map_print import VT_Map_Print
from vt_map_print import config

if __name__ == '__main__':
    printer = VT_Map_Print()
    # parsed = printer.parse_args(sys.argv[1:])
    # pprint("the type is {}".format(type(parsed)))
    printer.run_vt_map_print(sys.argv[1:])
