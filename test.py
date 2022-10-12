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
            # return map(lambda line: parseAgency(line), lines)
            return map(self.parseAgency, lines)

    @staticmethod
    def parseAgency(line):
        tokens = line.strip().split(", ")
        print(tokens)
        return SpaceAgency(tokens[0],  float(tokens[1]), float(tokens[2]))


if __name__ == "__main__":

    newAgency = SpaceAgenciesManager()
    # newAgency.addAgency("test", 12, 4)
    newAgency.removeAgency("test")
