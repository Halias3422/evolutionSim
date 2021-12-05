def createMapRepresentation(mapSizeX, mapSizeY):
    mapRepresentation = [[0 for x in range(mapSizeX)] for y in range(mapSizeY)]
    return mapRepresentation

def addPopulationListToMapRepresentation(populationList, mapRepresentation):
    for individual in populationList:
        mapRepresentation[individual.mapPosition[0]][individual.mapPosition[1]] = 1
    return mapRepresentation

def addFoodListToMapRepresentation(foodList, mapRepresentation):
    for food in foodList:
        mapRepresentation[food[0]][food[1]] = 2
    return mapRepresentation
