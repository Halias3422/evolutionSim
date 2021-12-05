from .individual import Individual
import random


def spawnNewGeneration(populationNb, mapSizeX, mapSizeY, parent):
    populationList = []
    while (populationNb > 0):
        if (parent is None):
            while True:
                individual = Individual(mapSizeX, mapSizeY, 0)
                if individual.currMapPosition not in populationList:
                    populationList.append(individual)
                    populationNb -= 1
                    break
    return populationList


def runCurrentGenerationLife(populationList, generationLifeSpan,
                             mapRepresentation):
    while (generationLifeSpan > 0):
        for individual in populationList:
            if (individual.currentGoal == "none"):
                individual = setIndividualCurrentGoal(individual,
                                                      mapRepresentation)
            if (individual.currentGoal == "none"):
                individual = individualExecuteRandomMovement(individual,
                                                           mapRepresentation)
            else:
                individual = individualMoveToCurrentGoal(individual,
                                                         mapRepresentation)
            checkSurroundingsAndAct(individual, mapRepresentation)
        generationLifeSpan -= 1
    return populationList

# def checkSurroundingsAndAct(individual, mapRepresentation):
#     if (individual.currentGoal == "food")


def individualMoveToCurrentGoal(individual, mapRepresentation):
    # set diagonal movements
    targetPos = individual.currGoalPos
    currPos = individual.currMapPosition
    movementPool = individual.genePool.movement
    newMovement = "none"
    if ("down" in movementPool and targetPos[0] > currPos[0]):
        newMovement = "down"
    elif ("up" in movementPool and targetPos[0] < currPos[0]):
        newMovement = "up"
    elif ("left" in movementPool and targetPos[1] < currPos[1]):
        newMovement = "left"
    elif ("right" in movementPool and targetPos[1] > currPos[1]):
        newMovement = "right"
    individual.setCurrentMovement(newMovement, mapRepresentation)


def individualExecuteRandomMovement(individual, mapRepresentation):
    movementOptions = len(individual.genePool.movement)
    movementPick = random.randint(0, movementOptions - 1)
    individual.setCurrentMovement(individual.genePool.movement[movementPick],
                                  mapRepresentation)
    return individual


def setIndividualCurrentGoal(individual, mapRepresentation):
    reproductionTargetPos = scanForTargetOnMap(individual,
                                               individual.genePool.reproductionRadar,
                                               1,
                                               mapRepresentation)
    foodTargetPos = scanForTargetOnMap(individual,
                                       individual.genePool.foodRadar,
                                       2,
                                       mapRepresentation)
    individual = chooseCurrentGoal(individual,
                                   reproductionTargetPos,
                                   foodTargetPos)

    return individual
        # RESUME WORK HERE NEED TO ADD NEXT TARGETS RECOGNITION


def chooseCurrentGoal(individual, foodTargetPos,
                      reproductionTargetPos):
    if (reproductionTargetPos is None and foodTargetPos is not None):
        individual.setCurrentGoal("food", foodTargetPos)
    elif (foodTargetPos is None and reproductionTargetPos is not None):
        individual.setCurrentGoal("reproduction", reproductionTargetPos)
    elif (foodTargetPos is not None and reproductionTargetPos is not None):
        individual = usePreferenceToChooseCurrentGoal(individual,
                                                      foodTargetPos,
                                                      reproductionTargetPos)
    else:
        individual.setCurrentGoal("none", None)
    return individual


def usePreferenceToChooseCurrentGoal(individual, foodTargetPos,
                                     reproductionTargetPos):
    preference = individual.genePool.preference
    randPreferencePick = random.randint(0, 10)
    if (preference > 5 and randPreferencePick <= preference):
        individual.setCurrentGoal("reproduction", reproductionTargetPos)
    elif (preference < 5 and randPreferencePick >= preference):
        individual.setCurrentGoal("food", foodTargetPos)
    elif (preference == 5):
        randPrefSetter = random.randint(0, 1)
        if (randPrefSetter == 0):
            individual.setCurrentGoal("reproduction", reproductionTargetPos)
        else:
            individual.setCurrentGoal("food", foodTargetPos)
    return individual


def scanForTargetOnMap(individual, geneRadar, targetCode, mapRepresentation):
    if (geneRadar > 0):
        for distance in range(1, geneRadar + 1):
            for coordX in range(-distance, distance + 1):
                for coordY in range(-distance, distance + 1):
                    if (checkIfTargetPositionIsValid(individual, coordX,
                                                     coordY, mapRepresentation)):
                        if (mapRepresentation[individual.currMapPosition[0] + coordY]
                                [individual.currMapPosition[1] + coordX] == targetCode):
                            return ([individual.currMapPosition[0] + coordY,
                                    individual.currMapPosition[1] + coordX])
    return None


def checkIfTargetPositionIsValid(individual, coordX, coordY,
                                 mapRepresentation):
    if (coordX == 0 and coordY == 0):
        return False
    maxCoordY = len(mapRepresentation) - 1
    maxCoordX = len(mapRepresentation[0]) - 1
    if (individual.currMapPosition[0] + coordY > maxCoordY
            or individual.currMapPosition[1] + coordX > maxCoordX):
        return False
    return True
