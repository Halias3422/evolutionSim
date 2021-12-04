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
                             mapSizeX, mapSizeY):
    populationMap = createCurrLifeSpanMap(populationList, mapSizeX, mapSizeY)
    while (generationLifeSpan > 0):
        for individual in populationList:
            if (individual.currentGoal == ""):
                setIndividualCurrentGoal(individual, populationList,
                                         populationMap)
        generationLifeSpan -= 1


def createCurrLifeSpanMap(populationList, mapSizeX, mapSizeY):
    currMap = [[0 for x in range(mapSizeX)] for y in range(mapSizeY)]
    for individual in populationList:
        currMap[individual.mapPosition[0]][individual.mapPosition[1]] = 1


def setIndividualCurrentGoal(individual, populationList, populationMap):
    if (individual.genePool.reproductionRadar > 0):
        reproductionTargetPos = scanForReproductionTarget(individual,
                                                          populationList,
                                                          populationMap)
        # RESUME WORK HERE NEED TO ADD NEXT TARGETS RECOGNITION


def scanForReproductionTarget(individual, populationList, populationMap):
    for distance in range(1, individual.genePool.reproductionRadar + 1):
        for coordX in range(-distance, distance + 1):
            for coordY in range(-distance, distance + 1):
                if (coordX != 0 or coordY != 0):
                    if (populationMap[coordY][coordX] == 1):
                        return ([coordY, coordX])



