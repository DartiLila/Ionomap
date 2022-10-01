from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from osgeo import gdal
from numpy import linspace
from numpy import meshgrid

# Create the map // mos harro ne fund res = i
map = Basemap(projection='kav7',lon_0=0,resolution='c')

# Color the map acording to area (Continents green, ocans and lakes black)
map.drawmapboundary(fill_color='black')
map.fillcontinents(color='green', lake_color='black')
map.drawcoastlines()

# Create the meridians and parallels and name them
map.drawparallels(np.arange(-90., 91., 30.), labels=[1, 1, 0, 1], color='white', textcolor='black')
map.drawmeridians(np.arange(-180., 181., 60.), labels=[1, 1, 0, 1], color='white', textcolor='black')

# Coordinates for cities: London, Berlin, Paris, NYC, Austin, LA,
lons = [-0.1, 10, -20, -20]
lats = [51, -10, 40, -20]

x, y = map(lons, lats)

map.scatter(x, y, marker='o', color='r',  markersize=10)


plt.title("Ionosphere Projection")
plt.show()
plt.savefig('test.png')
