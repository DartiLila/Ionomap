from netCDF4 import Dataset

dataSet = Dataset('/Users/User/Documents/GitHub/Ionomap/exampleData/dataset1.nc')

ionovars = dataSet.variables['percent_of_normal']
data = 0.01 * ionovars[:]
latcorners = dataSet.variables['y'][:]
loncorners = -dataSet.variables['x'][:]

if __name__ == "__main__":

    # for dim in dataSet.dimensions.values():
    #     print(dim)
    # print(dataSet)
    for var in dataSet.variables.values():
        print(var)

