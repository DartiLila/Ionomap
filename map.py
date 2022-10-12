from mpl_toolkits.basemap import Basemap, cm
import matplotlib.pyplot as plt
import numpy as np
from netCDF4 import Dataset as NetCDFFile


class SpaceAgenciesData:
    def __init__(self, agencyName, agencyLongtitute, agencyLatitude,
                 fileName='C:/Users/User/Documents/GitHub/Ionomap/assets/SpaceAgencies.txt'):
        self.agencyName = agencyName
        self.agencyLatitude = agencyLongtitute
        self.agencyLatitude = agencyLatitude
        self.fileName = fileName

    def addAgency(self, agencyName, agencyLongtitute, agencyLatitude, fileName):
        with open(fileName, "w") as textFile:
            lines = textFile.readlines()

            for line in lines[::-1]:
                lines.append(f"{agencyName}: {agencyLatitude}, {agencyLongtitute} \n")
                break

        pass

    def removeAgency(self, agencyName, fileName):
        pass

    def checkIfExist(self, agencyName, fileName):
        pass

    def agencyInfo(self, agencyName, fileName):
        pass


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

# x, y = m(lons, lats)

# m.scatter(x, y, marker='o', color='m')

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
plt.savefig('C:/Users/User/Documents/GitHub/Ionomap/assets/Map.png', facecolor="black", edgecolor="green")
