from mpl_toolkits.basemap import Basemap, cm
import matplotlib.pyplot as pyplot
import numpy
from CNDataAnalysys import *
from SpaceAgencyManager import *

for line in Agencies.agenciesObjCreator():
    longitudes.append(line.getLatitudes())
    latitudes.append(line.getLongitudes())

fig = pyplot.figure(figsize=(8, 8))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

map = Basemap(projection='kav7', lon_0=0, resolution='i')

map.drawmapboundary(fill_color='black')
map.fillcontinents(color='green', lake_color='black')
map.drawcoastlines()

map.drawparallels(numpy.arange(-90., 91., 30.), labels=[1, 1, 0, 1], color='white', textcolor='white')
map.drawmeridians(numpy.arange(-180., 181., 60.), labels=[1, 1, 0, 1], color='white', textcolor='white')

x, y = map(longitudes, latitudes)
map.scatter(x, y, marker='o', color='m')

ny = data.shape[0]
nx = data.shape[1]
lons, lats = map.makegrid(nx, ny)
xx, yy = map(lons, lats)

clevs = [0, 1, 2.5, 5, 7.5, 10, 15, 20, 30, 40, 50, 70, 100, 150, 200, 250, 300, 400, 500, 600, 750]
cs = map.contourf(xx, yy, data, clevs, cmap=cm.s3pcpn)
cbar = map.colorbar(cs, location='bottom', pad="5%")
cbar.set_label('AER')

pyplot.title('Ionosphere Projection')
pyplot.savefig('C:/Users/User/Documents/GitHub/Ionomap/assets/Map.png', facecolor="black", edgecolor="green")
