#!/usr/bin/python3
import polygonal
import sys

polygoner = polygonal.PolygonalImage()
parameter: str = sys.argv[1]

if parameter.__contains__(' -f '):
    polygoner.search_polygons(parameter.replace(' -f ', ''))
    polygoner.get_polygons()
else:
    print(f'Usage: {sys.argv[0]} -f <file_name>.png')    