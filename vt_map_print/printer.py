import requests
import glob, os
import numpy as np
from PIL import Image, ImageFile
import argparse
ImageFile.LOAD_TRUNCATED_IMAGES = True

from vt_map_print.third_party import globalMapTiles3
from vt_map_print import config

class VT_Map_Print():

    def __init__(self):
        self.gmt = globalMapTiles3.GlobalMercator()


    def run_vt_map_print(self, args):
        self.parsed = self.parse_args(args)
        self.define_arguments()
        tile_count = self.tile_count(self.zoom, self.tl_lat, self.tl_lon, self.br_lat, self.br_lon)
        print("the tile count is {}".format(tile_count))
        if tile_count > 100:
            print("Your request is too large.  It will return {} many tiles.  Plese choose a smaller zoom level".format(tile_count))
            return
        top_left = self.tile_from_lat_lon(self.tl_lat, self.tl_lon, self.zoom)
        bottom_right = self.tile_from_lat_lon(self.br_lat, self.br_lon, self.zoom)
        print(top_left[0], bottom_right[0], top_left[1], bottom_right[1], self.parsed.zoom)
        self.make_map(top_left[0], bottom_right[0], top_left[1], bottom_right[1], self.zoom, self.api_token)


    def save_tile(self, x, y):
        url = "{}/{}/tiles/{}/{}/{}/{}{}?access_token={}".format(self.mapbox_url, self.style_id, self.pixels,
                                                            self.zoom, x, y, self.retina, self.api_token)
        print(url)
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open('{}_{}_{}.png'.format(self.zoom, x, y), 'wb') as out_file:
                out_file.write(r.content)
                try:
                    im = Image.open('{}_{}_{}.png'.format(self.zoom, x, y))
                    rgb_im = im.convert('RGBA')
                    rgb_im.save('{}_{}_{}.png'.format(self.zoom, x, y))
                except:
                    out_file.close()
                    im = Image.open('{}_{}_{}.png'.format(self.zoom, x, y))
                    rgb_im = im.convert('RGBA')
                    rgb_im.save('{}_{}_{}.png'.format(self.zoom, x, y))


    def put_tiles_together(self, y, numRows):
        hori_list = []
        for i in range(numRows):
            y_value = y + i
            imgs = []
            for file in glob.glob("*_{}.png".format(y_value)):
                print(file)
                imgs.append(Image.open(file))
            imgs = np.hstack( (imgs) )
            hori_list.append(imgs)

        v_stack = np.vstack(hori_list)
        v_stack = Image.fromarray( v_stack )
        v_stack.save( 'mapGrid_real.png' )


    def make_map(self, x1, x2, y1, y2, zoom, api_token):
        os.chdir("images")
        for x in range(x1, x2):
            for y in range(y1, y2):
                self.save_tile(x, y)
                print("({}, {})".format(x, y))
        print(y1, y2-y1)
        self.put_tiles_together(y1, y2-y1)


    def tile_from_lat_lon(self, lat, lon, zoom):
        meters = self.gmt.LatLonToMeters(lat, lon)
        pixels = self.gmt.MetersToPixels(meters[0], meters[1], zoom)
        tiles = self.gmt.PixelsToTile(pixels[0], pixels[1])
        google_tiles = self.gmt.GoogleTile(tiles[0], tiles[1], zoom)
        print(google_tiles)
        return google_tiles


    def parse_args(self, args):
        parser = argparse.ArgumentParser()
        # parser.add_argument("--api_token", help="your mapbox api token")
        parser.add_argument("zoom", help="your mapbox api token", type=int)
        parser.add_argument("top_left_lat", help="the latitudinal position of the top left point in your bbox", type=float)
        parser.add_argument("top_left_lon", help="the longitudinal position of the top left point in your bbox", type=float)
        parser.add_argument("bottom_right_lat", help="the latitudinal position of the bottom right point in your bbox", type=float)
        parser.add_argument("bottom_right_lon", help="the longitudinal position of the bottom right point in your bbox", type=float)
        parser.add_argument("-a", "--api_token", help="override the config api_token with another Mapbox API Token")
        parser.add_argument("-p", "--pixels", help="number of pixels in tile - accepts '256' or '512'")
        parser.add_argument("-r", "--retina", help="accepts 'Y' or 'N' default is N")
        parser.add_argument("-s", "--style_id", help="specify the Mabox Style ID default is streets")
        parser.add_argument("-u", "--mapbox_url", help="override the config mapbox_url with another Mapbox url")
        return parser.parse_args()


    def define_arguments(self):
        self.zoom = self.parsed.zoom
        self.tl_lat = self.parsed.top_left_lat
        self.tl_lon = self.parsed.top_left_lon
        self.br_lat = self.parsed.bottom_right_lat
        self.br_lon = self.parsed.bottom_right_lon

        ## optional
        self.api_token = self.parsed.api_token if self.parsed.api_token else config.api_token
        self.pixels = self.parsed.pixels if self.parsed.pixels else 256
        self.retina = "@2x" if self.parsed.retina == "Y" else ""
        self.style_id = self.parsed.style_id if self.parsed.style_id else "cj49edx972r632rp904oj4acj" #change to streets
        self.mapbox_url = self.parsed.mapbox_url if self.parsed.mapbox_url else config.mapbox_url
        print("{} and the args is {}".format(self.retina, self.parsed.retina))


    def tile_count(self, zoom, tl_lat, tl_lon, br_lat, br_lon):
        top_left = self.tile_from_lat_lon(tl_lat, tl_lon, zoom)
        bottom_right = self.tile_from_lat_lon(br_lat, br_lon, zoom)
        x = bottom_right[0] - top_left[0]
        y = bottom_right[1] - top_left[1]
        return x * y


    #@TODO
    def pixel_count(self):
        pass
