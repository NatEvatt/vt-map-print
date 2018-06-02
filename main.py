import argparse
from vt_map_print import vt_map_print

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument("--api_token", help="your mapbox api token")
    parser.add_argument("zoom", help="your mapbox api token", type=int)
    parser.add_argument("top_left_lat", help="the latitudinal position of the top left point in your bbox", type=float)
    parser.add_argument("top_left_lon", help="the longitudinal position of the top left point in your bbox", type=float)
    parser.add_argument("bottom_right_lat", help="the latitudinal position of the bottom right point in your bbox", type=float)
    parser.add_argument("bottom_right_lon", help="the longitudinal position of the bottom right point in your bbox", type=float)
    args = parser.parse_args()
    # print("the mapbox api token is {}".format(args.zoom))
    # print(type(args.zoom))
    vt_map_print.run_vt_map_print(args.zoom, args.top_left_lat, args.top_left_lon, args.bottom_right_lat, args.bottom_right_lon)
