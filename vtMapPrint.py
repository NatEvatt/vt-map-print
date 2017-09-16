import requests
import shutil
import glob, os
import numpy as np
from PIL import Image
from globalMapTiles3 import GlobalMercator
gmt = GlobalMercator()

def saveTile(zoom, x, y):
    pixels = 256
    retina = '@2x'
    styleId = "cj49edx972r632rp904oj4acj"
    apiToken = "pk.eyJ1IjoibmF0ZXZhdHQiLCJhIjoiR1hVR1ZIdyJ9.gFwSyghJZIERfjLkzgTx6A"
    url = "https://api.mapbox.com/styles/v1/natevatt/{}/tiles/{}/{}/{}/{}{}?access_token={}".format(styleId, pixels, zoom, x, y, retina, apiToken)
    print(url)
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open('{}_{}_{}.png'.format(zoom, x, y), 'wb') as out_file:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, out_file)
            im = Image.open('{}_{}_{}.png'.format(zoom, x, y))
            rgb_im = im.convert('RGB')
            rgb_im.save('{}_{}_{}.png'.format(zoom, x, y))

def putTilesTogether(y, numRows):
    hori_list = []
    for i in range(numRows):
        yValue = y + i
        imgs = []
        for file in glob.glob("*_{}.png".format(yValue)):
            print(file)
            imgs.append(Image.open(file))
        imgs = np.hstack( (imgs) )
        hori_list.append(imgs)

    vStack = np.vstack(hori_list)
    vStack = Image.fromarray( vStack )
    vStack.save( 'mapGrid_real.png' )

def makeMap(x1, x2, y1, y2, zoom):
    os.chdir("images")
    for x in range(x1, x2):
        for y in range(y1, y2):
            saveTile(zoom, x, y)
            print("({}, {})".format(x, y))
    print(y1, y2-y1)
    putTilesTogether(y1, y2-y1)

def tileFromLatLon(lat, lon, zoom):
    meters = gmt.LatLonToMeters(lat, lon)
    # print(meters)
    pixels = gmt.MetersToPixels(meters[0], meters[1], zoom)
    # print(pixels)
    tiles = gmt.PixelsToTile(pixels[0], pixels[1])
    googleTiles = gmt.GoogleTile(tiles[0], tiles[1], zoom)
    print(googleTiles)
    return googleTiles

zoom = 14
topLeft = tileFromLatLon(36.985003092, -122.0581054, zoom)
bottomRight = tileFromLatLon(36.949891786, -121.9702148, zoom)

print(topLeft[0], bottomRight[0], topLeft[1], bottomRight[1], zoom)
makeMap(topLeft[0], bottomRight[0], topLeft[1], bottomRight[1], zoom)
