def printIndividualGenePool(individual):
    print("Movement = " + individual.genePool.movement)
    print("dangerRadar = " + str(individual.genePool.dangerRadar))
    print("foodRadar = " + str(individual.genePool.foodRadar))
    print("reproductionRadar = " + str(individual.genePool.reproductionRadar))
    print("fertility = " + str(individual.genePool.fertility))

def printPopulationListPositions(populationList):
    for individual in populationList:
        print(individual.mapPosition)
