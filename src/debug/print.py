def printIndividualGenePool(individual):
    print("Movement = " + individual.genePool.movement)
    print("dangerRadar = " + str(individual.genePool.dangerRadar))
    print("foodRadar = " + str(individual.genePool.foodRadar))
    print("reproductionRadar = " + str(individual.genePool.reproductionRadar))
    print("fertility = " + str(individual.genePool.fertility))


def printPopulationListPositions(populationList, loopIndex):
    for individual in populationList:
        print("individualPos = " + str(individual.mapPosition[loopIndex]))


def printPopulationListCurrentGoal(populationList):
    for individual in populationList:
        print("individualCurrentGoal = " + individual.currentGoal)


def printFoodListPositions(foodList):
    for food in foodList:
        print("foodPos = " + str(food))


def printDataCollectionForCurrentGeneration(dataCollection):
    print("Population Size = " + str(dataCollection.populationSize))
    print("Individuals that have reproduced = "
          + str(dataCollection.hasReproducedNb))
    print("Individuals that have eaten = "
          + str(dataCollection.hasEatenNb))
    print("Individuals that have both reproduced and eaten = "
          + str(dataCollection.hasReproducedAndEatenNb))
