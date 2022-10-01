from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# Create the map
map = Basemap(projection='kav7',lon_0=0,resolution='i')

# Color the map acording to area (Continents green, ocans and lakes black)
map.drawmapboundary(fill_color='black')
map.fillcontinents(color='green', lake_color='black')
map.drawcoastlines()

# Create the meridians and parallels and name them
map.drawparallels(np.arange(-90., 91., 30.), labels=[1, 1, 0, 1], color='white', textcolor='black')
map.drawmeridians(np.arange(-180., 181., 60.), labels=[1, 1, 0, 1], color='white', textcolor='black')

lons = [0, 10, -20, -20]
lats = [0, -10, 40, -20]

map.plot(lons, lats, marker='D', color='r')


plt.title("Ionosphere Projection")
plt.show()
plt.savefig('test.png')
