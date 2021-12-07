from .individual import Individual
from environment.mapRepresentation import updateMapRepresentation
import random


def spawnNewGeneration(populationNb, mapSizeX, mapSizeY, generationLifeSpan,
                       parent):
    populationList = []
    while (populationNb > 0):
        if (parent is None):
            while True:
                individual = Individual(mapSizeX, mapSizeY, 0,
                                        generationLifeSpan, populationNb)
                if individual.currMapPosition not in populationList:
                    populationList.append(individual)
                    populationNb -= 1
                    break
    return populationList


def runCurrentGenerationLife(populationList, generationLifeSpan,
                             mapRepresentation, foodList):
    loopIndex = 0
    while (loopIndex < generationLifeSpan):
        initialFoodList = foodList[loopIndex][:]
        if (loopIndex > 0):
            for individual in populationList:
                if (individual.currentGoal == "none"):
                    individual = setIndividualCurrentGoal(individual,
                                                          mapRepresentation,
                                                          populationList)
                if (individual.currentGoal == "none"):
                    individual = individualExecuteRandomMovement(individual,
                                                                 mapRepresentation,
                                                                 populationList)
                else:
                    individual = individualMoveToCurrentGoal(individual,
                                                             mapRepresentation,
                                                             populationList)
                individual = checkSurroundingsAndAct(individual, mapRepresentation,
                                                     initialFoodList,
                                                     populationList,
                                                     loopIndex)
        foodList.append(initialFoodList)
        mapRepresentation = updateMapRepresentation(mapRepresentation,
                                                    populationList, foodList,
                                                    loopIndex)
        loopIndex += 1
    return populationList


def checkSurroundingsAndAct(individual, mapRepresentation, foodList,
                            populationList, loopIndex):
    if (individual.currentGoal == "food"):
        targetAcquired = scanAdjacentTilesForTarget(individual.currMapPosition,
                                                    "food", mapRepresentation)
        if (targetAcquired and foodIsStillThere(targetAcquired, foodList)):
            individual.eats(loopIndex)
            foodList.remove(targetAcquired)
            individual.currentGoal = "none"
            mapRepresentation[targetAcquired[0]][targetAcquired[1]] == "empty"
    elif (individual.currentGoal == "reproduction"):
        targetAcquired = scanAdjacentTilesForTarget(individual.currMapPosition,
                                                    "individual",
                                                    mapRepresentation)
        if (targetAcquired):
            reproductionPartner = identifyReproductionPartner(individual,
                                                              targetAcquired,
                                                              populationList,
                                                              loopIndex)
            if (reproductionPartner):
                individual.reproduces(reproductionPartner, loopIndex)
                individual.currentGoal = "none"
    return individual


def foodIsStillThere(targetAcquired, foodList):
    if (targetAcquired in foodList):
        return True
    return False


def identifyReproductionPartner(individual, targetCoord, populationList,
                                loopIndex):
    for partner in populationList:
        if (partner.currMapPosition == targetCoord):
            partner.reproduces(individual, loopIndex)
            if (partner.currentGoal == "reproduction"):
                partner.currentGoal = "none"
            return partner


def scanAdjacentTilesForTarget(currPosition, targetName, mapRepresentation):
    mapSizeY = len(mapRepresentation)
    mapSizeX = len(mapRepresentation[0])
    if (currPosition[0] - 1 >= 0
        and mapRepresentation[currPosition[0] - 1][currPosition[1]]
            == targetName):
        return ([currPosition[0] - 1, currPosition[1]])
    elif (currPosition[0] + 1 < mapSizeY
          and mapRepresentation[currPosition[0] + 1][currPosition[1]]
          == targetName):
        return ([currPosition[0] + 1, currPosition[1]])
    elif (currPosition[1] - 1 >= 0
          and mapRepresentation[currPosition[0]][currPosition[1] - 1]
          == targetName):
        return ([currPosition[0], currPosition[1] - 1])
    elif (currPosition[1] + 1 < mapSizeX
          and mapRepresentation[currPosition[0]][currPosition[1] + 1]
          == targetName):
        return ([currPosition[0], currPosition[1] + 1])
    else:
        return None


def individualMoveToCurrentGoal(individual, mapRepresentation, populationList):
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
    individual.setCurrentMovement(newMovement, mapRepresentation,
                                  populationList)
    return individual


def individualExecuteRandomMovement(individual, mapRepresentation,
                                    populationList):
    movementOptions = len(individual.genePool.movement)
    movementPick = random.randint(0, movementOptions - 1)
    individual.setCurrentMovement(individual.genePool.movement[movementPick],
                                  mapRepresentation, populationList)
    return individual


def setIndividualCurrentGoal(individual, mapRepresentation, populationList):
    reproductionTargetPos = None
    foodTargetPos = None
    if (individual.hasReproduced is False):
        reproductionTargetPos = scanForTargetOnMap(individual,
                                                   individual.genePool.reproductionRadar,
                                                   "individual",
                                                   mapRepresentation,
                                                   populationList)
    if (individual.hasEaten is False):
        foodTargetPos = scanForTargetOnMap(individual,
                                           individual.genePool.foodRadar,
                                           "food",
                                           mapRepresentation,
                                           populationList)
    individual = chooseCurrentGoal(individual,
                                   reproductionTargetPos,
                                   foodTargetPos)
    return individual


def chooseCurrentGoal(individual, reproductionTargetPos, foodTargetPos):
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


def scanForTargetOnMap(individual, geneRadar, targetCode, mapRepresentation,
                       populationList):
    if (geneRadar > 0):
        for distance in range(1, geneRadar + 1):
            for coordX in range(-distance, distance + 1):
                for coordY in range(-distance, distance + 1):
                    if (checkIfTargetPositionIsValid(individual, coordX,
                                                     coordY, mapRepresentation)):
                        if (mapRepresentation[individual.currMapPosition[0] + coordY]
                                [individual.currMapPosition[1] + coordX] == targetCode):
                            if (targetCode != "individual"
                                or checkIfTargetHasReproduced([individual.currMapPosition[0] + coordY,
                                    individual.currMapPosition[1] + coordX],
                                    populationList)):
                                return ([individual.currMapPosition[0] + coordY,
                                        individual.currMapPosition[1] + coordX])
    return None

def checkIfTargetHasReproduced(targetCoord, populationList):
    for target in populationList:
        if (target.currMapPosition == targetCoord):
            if (target.hasReproduced is False):
                return True
    return False


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

def removeAllUnsuccessfullIndividuals(populationList):
    successfullPopulationList = []
    for individual in populationList:
        if (individual.hasEaten is True and individual.hasReproduced is True):
            successfullPopulationList.append(individual)
    print("success = " + str(len(successfullPopulationList)))
    return successfullPopulationList
