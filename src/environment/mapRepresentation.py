def updateMapRepresentation(mapRepresentation, populationList, foodList,
                            loopIndex):
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
    return mapRepresentation

def createMapRepresentation(mapSizeX, mapSizeY):
    mapRepresentation = [["empty" for x in range(mapSizeX)] for y in range(mapSizeY)]
    return mapRepresentation


def addPopulationListToMapRepresentation(populationList, mapRepresentation):
    for individual in populationList:
        mapRepresentation[individual.currMapPosition[0]][individual.currMapPosition[1]] = "individual"
    return mapRepresentation


def addFoodListToMapRepresentation(foodList, mapRepresentation):
    for food in foodList:
        mapRepresentation[food[0]][food[1]] = "food"
    return mapRepresentation
