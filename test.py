class SpaceAgency:
    def __init__(self, name, longitude, latitude):
        self.name = name
        self.longitude = longitude
        self.latitude = latitude

    def getValues(self):
        print(self.name, self.longitude, self.latitude)


class SpaceAgenciesManager:
    def __init__(self, fileName='C:/Users/User/Documents/GitHub/Ionomap/assets/SpaceAgencies.txt'):
        self.fileName = fileName

    def addAgency(self, name, longitude, latitude):
        if not type(name) is str:
            raise TypeError("Attribute 'name' must be string")
        if not type(longitude) and type(latitude) is int or float:
            raise TypeError("Attribute 'longitude' and 'latitude' must be int or float")
        with open(self.fileName, "a") as textFile:
            agency = f"\n{name}, {longitude}, {latitude}"
            textFile.write(agency)

    def removeAgency(self, name):
        with open(self.fileName, "r+") as textFile:
            lines = textFile.readlines()
            textFile.seek(0)
            textFile.write("")
            textFile.truncate()
            for line in lines:
                if name not in line:
                    with open(self.fileName, "a") as textFile1:
                        textFile1.write(line)
            return print("Delete successful!")

    def agenciesObjCreator(self):
        with open(self.fileName, "r") as textFile:
            lines = textFile.readlines()
            return map(self.parseAgency, lines)

    @staticmethod
    def parseAgency(line):
        tokens = line.strip().split(",")
        print(tokens)
        return SpaceAgency(tokens[0], float(tokens[1]), float(tokens[2]))


if __name__ == "__main__":
    newAgency = SpaceAgenciesManager()
    newAgency.addAgency("hep", 3, 5)

    # newAgency.addAgency("test", 12, 4)
    # newAgency.removeAgency("test")
