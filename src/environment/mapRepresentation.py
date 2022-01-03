import random

def updateMapRepresentation(mapRepresentation, populationList, foodList,
                            loopIndex, mainData):
    mapSizeY = len(mapRepresentation) - 1
    while (mapSizeY >= 0):
        mapSizeX = len(mapRepresentation[0]) - 1
        while (mapSizeX >= 0):
            mapRepresentation[mapSizeY][mapSizeX] = "empty"
            mapSizeX -= 1
        mapSizeY -= 1
    mapRepresentation = addPopulationListToMapRepresentation(populationList,
                                                             mapRepresentation)
    mapRepresentation = addFoodListToMapRepresentation(foodList[loopIndex],
                                                       mapRepresentation)
    mapRepresentation = addObstacleListToMapRepresentation(mainData.obstacleList,
                                                           mapRepresentation)
    return mapRepresentation

def createMapRepresentation(mapSizeX, mapSizeY):
    mapRepresentation = [["empty" for x in range(mapSizeX)] for y in range(mapSizeY)]
    return mapRepresentation

def addObstacleListToMapRepresentation(obstacleList, mapRepresentation):
    for obstacle in obstacleList:
        mapRepresentation[obstacle[0]][obstacle[1]] = "obstacle"
    return mapRepresentation

def addPopulationListToMapRepresentation(populationList, mapRepresentation):
    for individual in populationList:
        mapRepresentation[individual.currMapPosition[0]][individual.currMapPosition[1]] = "individual"
    return mapRepresentation


def addFoodListToMapRepresentation(foodList, mapRepresentation):
    for food in foodList:
        mapRepresentation[food[0]][food[1]] = "food"
    return mapRepresentation

def addZonesToMapRepresentationCurrGen(mainData):
    currY = mainData.mapSizeY - 1
    while (currY >= 0):
        currX = mainData.mapSizeX - 1
        while (currX >= 0):
            mainData.mapRepresentation[currY][currX] = \
                mainData.zonesMapRepresentation[currY][currX]
            if (mainData.zonesMapRepresentation[currY][currX] == "obstacle"):
                mainData.obstacleList.append([currY, currX])
            if (mainData.dangerZoneMapRepresentation[currY][currX] == "danger"):
                mainData.dangerList.append([currY, currX])
            currX -= 1
        currY -= 1
    return mainData.mapRepresentation

def generateDangerZoneMap(mainData):
    dangerMap = createMapRepresentation(mainData.mapSizeX, mainData.mapSizeY)
    dangerTiles = 0
    while (dangerTiles < mainData.dangerNb):
        while (True):
            newTile = [random.randint(0, mainData.mapSizeY - 1),
                       random.randint(0, mainData.mapSizeX - 1)]
            if (dangerMap[newTile[0]][newTile[1]] == "empty"):
                dangerMap[newTile[0]][newTile[1]] = "danger"
                dangerTiles += 1
                break
    return dangerMap

def getMapFreeTilesNumber(map, sizeX, sizeY):
    currY = 0
    freeTilesNb = 0
    while (currY < sizeY):
        currX = 0
        while (currX < sizeX):
            if (map[currY][currX] == "empty"):
                freeTilesNb += 1
            currX += 1
        currY += 1
    return freeTilesNb

def addRandomZoneToZoneMap(mainData, zoneType, zoneNb):
    zoneMap = mainData.zonesMapRepresentation
    zoneTiles = 0
    freeTilesNb = getMapFreeTilesNumber(zoneMap, mainData.mapSizeX,
                                           mainData.mapSizeY)
    while (zoneTiles < zoneNb):
        while (True):
            if (freeTilesNb <= 0 ):
                return zoneMap
            newTile = [random.randint(0, mainData.mapSizeY - 1),
                       random.randint(0, mainData.mapSizeX - 1)]
            if (zoneMap[newTile[0]][newTile[1]] == "empty"):
                zoneMap[newTile[0]][newTile[1]] = zoneType
                zoneTiles += 1
                freeTilesNb -= 1
                break
    return zoneMap
