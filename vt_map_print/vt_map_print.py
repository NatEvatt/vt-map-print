import requests
import shutil
import glob, os
import numpy as np
from PIL import Image

from vt_map_print.third_party import globalMapTiles3
from vt_map_print import config

gmt = globalMapTiles3.GlobalMercator()

def save_tile(zoom, x, y):
    pixels = 256
    retina = '@2x'
    style_id = "cj49edx972r632rp904oj4acj"
    api_token = config.api_token
    url = "https://api.mapbox.com/styles/v1/natevatt/{}/tiles/{}/{}/{}/{}{}?access_token={}".format(style_id, pixels, zoom, x, y, retina, api_token)
    print(url)
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open('{}_{}_{}.png'.format(zoom, x, y), 'wb') as out_file:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, out_file)
            im = Image.open('{}_{}_{}.png'.format(zoom, x, y))
            rgb_im = im.convert('RGB')
            rgb_im.save('{}_{}_{}.png'.format(zoom, x, y))

def put_tiles_together(y, numRows):
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

def make_map(x1, x2, y1, y2, zoom):
    os.chdir("images")
    for x in range(x1, x2):
        for y in range(y1, y2):
            save_tile(zoom, x, y)
            print("({}, {})".format(x, y))
    print(y1, y2-y1)
    put_tiles_together(y1, y2-y1)

def tile_from_lat_lon(lat, lon, zoom):
    meters = gmt.LatLonToMeters(lat, lon)
    # print(meters)
    pixels = gmt.MetersToPixels(meters[0], meters[1], zoom)
    # print(pixels)
    tiles = gmt.PixelsToTile(pixels[0], pixels[1])
    google_tiles = gmt.GoogleTile(tiles[0], tiles[1], zoom)
    print(google_tiles)
    return google_tiles

def run_vt_map_print():
    zoom = 14
    top_left = tile_from_lat_lon(36.985003092, -122.0581054, zoom)
    bottom_right = tile_from_lat_lon(36.949891786, -121.9702148, zoom)

    print(top_left[0], bottom_right[0], top_left[1], bottom_right[1], zoom)
    make_map(top_left[0], bottom_right[0], top_left[1], bottom_right[1], zoom)
