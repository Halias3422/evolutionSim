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
            if (mainData.zonesMapRepresentation[currY][currX] == "obstacle"
                    and ([currY, currX]) not in mainData.obstacleList):
                mainData.obstacleList.append([currY, currX])
            if (mainData.dangerZoneMapRepresentation[currY][currX] == "danger"
                    and ([currY, currX]) not in mainData.dangerList):
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

def registerDangerTileLevel(tileX, tileY, dangerMap, applicationGUI):
    amplitude = 1
    while (True):
        currY = tileY - amplitude
        while (currY <= tileY + amplitude):
            currX = tileX - amplitude
            while (currX <= tileX + amplitude):
                if (currY >= 0 and currY < applicationGUI.mapSizeY
                        and currX >= 0 and currX < applicationGUI.mapSizeX):
                    if (dangerMap[currY][currX] == "empty"):
                        return (amplitude)
                currX += 1
            currY += 1
        amplitude += 1



def allTilesAreDanger(mainData, applicationGUI):
    currY = applicationGUI.mapSizeY - 1
    while (currY >= 0):
        currX = applicationGUI.mapSizeX - 1
        while (currX >= 0):
            if (mainData.dangerZoneMapRepresentation[currY][currX] == "empty"):
                return False
            currX -= 1
        currY -= 1
    return True


def generateDangerLevelMap(mainData, applicationGUI):
    dangerMap = mainData.dangerZoneMapRepresentation
    if (allTilesAreDanger(mainData, applicationGUI) is True):
        dangerLvlMap = [[1 for x in range(applicationGUI.mapSizeX)]
                for y in range(applicationGUI.mapSizeY)]
        return dangerLvlMap
    else:
        dangerLvlMap = [[0 for x in range(applicationGUI.mapSizeX)]
                for y in range(applicationGUI.mapSizeY)]
    currY = applicationGUI.mapSizeY - 1
    while (currY >= 0):
        currX = applicationGUI.mapSizeX - 1
        while (currX >= 0):
            if (dangerMap[currY][currX] == "danger"):
                dangerLvlMap[currY][currX] = registerDangerTileLevel(currX, currY,
                                                                     dangerMap,
                                                                     applicationGUI)
            currX -= 1
        currY -= 1
    return dangerLvlMap


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
