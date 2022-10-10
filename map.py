from mpl_toolkits.basemap import Basemap, cm
import matplotlib.pyplot as plt
import numpy as np
from netCDF4 import Dataset as NetCDFFile
"""
Coordinates for space agencies: NASA Mission Control Centre: 29.560034, -95.089188
                        Australian Space Center: -34.920288, 138.608255
                        Brazilian Space Agency: -15.815123, -47.943437
                        Canadian Space Agency: 45.520009, -73.393664
                        European Space Agency (France): 48.843610, 2.389846
                        Indian Space Research Organization: 13.035112, 77.570820
                        Japan Aerospace Exploration Agency: 48.873461, 2.306115
                        Mexican Aerospace Agency: 19.360946, -99.183290
                        National Space Activities Commission of Argentina: -34.616677, -58.369542
                        National Space Science Agency of Bahrain: 26.224290, 50.676696
                        Paraguayan Space Agency: -25.293470, -57.612809
                        South African Space Agency: -34.424128, 19.224627
"""
lons = [-95.089188, 138.608255, -47.943437, -73.393664, 2.389846, 77.570820, 2.306115, -99.183290, -58.369542,
        50.676696, -57.612809, 19.224627]
lats = [29.560034, -34.920288, -15.815123, 45.520009, 48.843610, 13.035112, 48.873461, 19.360946, -34.616677, 26.224290,
        -25.293470, -34.424128]


# Loads the data file
nc = NetCDFFile('/Users/User/Documents/GitHub/Ionomap/exampleData/dataset1.nc')

# Links to the data file
ionovar = nc.variables['percent_of_normal']
data = 0.01 * ionovar[:]
latcorners = nc.variables['y'][:]
loncorners = -nc.variables['x'][:]
# lon_0 = -nc.variables['normal'][:]
# lat_0 = nc.variables['observation'][:]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# Create the map
m = Basemap(projection='kav7', lon_0=0, resolution='i')

# Color the map acording to area (Continents green, ocans and lakes black)
m.drawmapboundary(fill_color='black')
m.fillcontinents(color='green', lake_color='black')
m.drawcoastlines()

# Create the meridians and parallels and name them
m.drawparallels(np.arange(-90., 91., 30.), labels=[1, 1, 0, 1], color='white', textcolor='white')
m.drawmeridians(np.arange(-180., 181., 60.), labels=[1, 1, 0, 1], color='white', textcolor='white')

x, y = m(lons, lats)

m.scatter(x, y, marker='o', color='m')

# Gets the specific coordinates and draws map
ny = data.shape[0]
nx = data.shape[1]
lons, lats = m.makegrid(nx, ny)  # get lat/lons of ny by nx evenly space grid.
xx, yy = m(lons, lats)  # compute map proj coordinates.


# Map legend
clevs = [0, 1, 2.5, 5, 7.5, 10, 15, 20, 30, 40, 50, 70, 100, 150, 200, 250, 300, 400, 500, 600, 750]
cs = m.contourf(xx, yy, data, clevs, cmap=cm.s3pcpn)

cbar = m.colorbar(cs, location='bottom', pad="5%")
cbar.set_label('AER')

plt.title('Ionosphere Projection')
plt.savefig('C:/Users/User/Documents/GitHub/Ionomap/assets/Map.png',facecolor="black", edgecolor="green")