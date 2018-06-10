# vt-map-print
This project uses the Mapbox Static API to export vector tile map styles as large / printable png files

## Installation
- Download or clone this repo
- Run `pip install -r requirements.txt`
- Create a `config.py` file similar to `config_example.py`

## Command Line Arguments
### Required Arguments
- **zoom**: zoom level of the map, type=int
- **top_left_lat**: the latitudinal position of the top left point in your bbox, type=float
- **top_left_lon**: the longitudinal position of the top left point in your bbox, type=float
- **bottom_right_lat**: the latitudinal position of the bottom right point in your bbox, type=float
- **bottom_right_lon**: the longitudinal position of the bottom right point in your bbox, type=float

### Optional Arguments
- **--api_token**, **-a**: override the config api_token with another Mapbox API Token
- **--pixels**, **-p**: number of pixels in tile - accepts '256' or '512'
- **--retina**, **-r**: retina display.  If set to true, a retina 2x image will be returned.  Accepts 'Y' or 'N' default is 'N')
- **--style_id**, **-s**: specify the Mapbox Style ID default is streets
- **--mapbox_url**, **-u**: override the config mapbox_url with another Mapbox url

## Example
Navigate inside of the first vt_map_print directory
Enter into the command line:  
`python3 main.py 14 36.985003092 -122.0581054 36.949891786 -121.9702148`
