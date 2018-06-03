import argparse
from vt_map_print import VT_Map_Print
# from vt_map_print import vt_map_print

if __name__ == '__main__':
    printer = VT_Map_Print()
    parser = argparse.ArgumentParser()
    # parser.add_argument("--api_token", help="your mapbox api token")
    parser.add_argument("zoom", help="your mapbox api token", type=int)
    parser.add_argument("top_left_lat", help="the latitudinal position of the top left point in your bbox", type=float)
    parser.add_argument("top_left_lon", help="the longitudinal position of the top left point in your bbox", type=float)
    parser.add_argument("bottom_right_lat", help="the latitudinal position of the bottom right point in your bbox", type=float)
    parser.add_argument("bottom_right_lon", help="the longitudinal position of the bottom right point in your bbox", type=float)
    parser.add_argument("-a", "--api_token", help="override the config api_token with another Mapbox API Token")
    parser.add_argument("-p", "--pixels", help="number of pixels in tile - accepts '256' or '512'")
    parser.add_argument("-r", "--retina", help="accepts '2' or '1' default is 2")
    parser.add_argument("-s", "--style", help="specify the Mabox Style ID default is streets")
    parser.add_argument("-u", "--mapbox_url", help="override the config mapbox_url with another Mapbox url")
    args = parser.parse_args()
    # api_token = args.api_token if args.api_token else config. 
    # print("the mapbox api token is {}".format(args.zoom))
    # print(type(args.zoom))
    printer.run_vt_map_print(args.zoom, args.top_left_lat, args.top_left_lon, args.bottom_right_lat, args.bottom_right_lon)
