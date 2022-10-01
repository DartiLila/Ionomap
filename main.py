from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap()

map.drawmapboundary(fill_color='black')
map.fillcontinents(color='green',lake_color='black')
map.drawcoastlines()


plt.show()
plt.savefig('test.png')
