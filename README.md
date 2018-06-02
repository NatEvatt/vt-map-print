# vt-map-print
This project uses the Mapbox Static API to export vector tile map styles as large / printable png files

## Installation
- Download or clone this repo
- Run `pip install -r requirements.txt`
- Create a `config.py` file similar to `config_example.py`

## Command Line Arguments
### Required
- **zoom**: zoom level of the map, type=int
- **top_left_lat**: the latitudinal position of the top left point in your bbox, type=float
- **top_left_lon**: the longitudinal position of the top left point in your bbox, type=float
- **bottom_right_lat**: the latitudinal position of the bottom right point in your bbox, type=float
- **bottom_right_lon**: the longitudinal position of the bottom right point in your bbox, type=float

## Example
Navigate inside of first vt_map_print
`python3 main.py 14 36.985003092 -122.0581054 36.949891786 -121.9702148`
