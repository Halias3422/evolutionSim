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
