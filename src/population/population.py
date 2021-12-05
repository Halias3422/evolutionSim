from .individual import Individual
from debug.print import printPopulationListPositions


def spawnNewGeneration(populationNb, mapSizeX, mapSizeY, parent):
    populationList = []
    while (populationNb > 0):
        if (parent is None):
            while True:
                individual = Individual(mapSizeX, mapSizeY, 0)
                if individual.mapPosition not in populationList:
                    populationList.append(individual)
                    populationNb -= 1
                    break
    return populationList


def runCurrentGenerationLife(populationList, generationLifeSpan,
                             mapSizeX, mapSizeY, mapRepresentation):
    while (generationLifeSpan > 0):
        for individual in populationList:
            if (individual.currentGoal == "none"):
                individual = setIndividualCurrentGoal(individual,
                                                      mapRepresentation)
        generationLifeSpan -= 1
    return populationList


def setIndividualCurrentGoal(individual, mapRepresentation):
    if (individual.genePool.reproductionRadar > 0):
        reproductionTargetPos = scanForTargetOnMap(individual,
                                                   individual.genePool.reproductionRadar,
                                                   1,
                                                   mapRepresentation)
        foodTargetPos = scanForTargetOnMap(individual,
                                           individual.genePool.foodRadar,
                                           2,
                                           mapRepresentation)
        if (reproductionTargetPos is None and foodTargetPos is not None):
            individual.setCurrentGoal("food", foodTargetPos)
        elif (foodTargetPos is None and reproductionTargetPos is not None):
            individual.setCurrentGoal("reproduction", reproductionTargetPos)
        else:
            individual.setCurrentGoal("none", None)
        return individual
        # RESUME WORK HERE NEED TO ADD NEXT TARGETS RECOGNITION


def scanForTargetOnMap(individual, geneRadar, targetCode, mapRepresentation):
    for distance in range(1, geneRadar + 1):
        for coordX in range(-distance, distance + 1):
            for coordY in range(-distance, distance + 1):
                if (checkIfTargetPositionIsValid(individual, coordX,
                                                 coordY, mapRepresentation)):
                    if (mapRepresentation[individual.mapPosition[0] + coordY]
                            [individual.mapPosition[1] + coordX] == targetCode):
                        return ([individual.mapPosition[0] + coordY,
                                individual.mapPosition[1] + coordX])
    return None


def checkIfTargetPositionIsValid(individual, coordX, coordY,
                                 mapRepresentation):
    if (coordX == 0 and coordY == 0):
        return False
    maxCoordY = len(mapRepresentation) - 1
    maxCoordX = len(mapRepresentation[0]) - 1
    if (individual.mapPosition[0] + coordY > maxCoordY
            or individual.mapPosition[1] + coordX > maxCoordX):
        return False
    return True
