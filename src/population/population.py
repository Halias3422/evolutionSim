from .individual import Individual


def initFirstGeneration(populationNb, mapSizeX, mapSizeY):
    populationList = []
    while (populationNb > 0):
        while True:
            individual = Individual(mapSizeX, mapSizeY)
            if individual.mapPosition not in populationList:
                populationList.append(individual)
                populationNb -= 1
                break
    return populationList
