from .individual import Individual
from .child import Child
from environment.mapRepresentation import updateMapRepresentation
import random

def checkIfCoordinateNotOccupied(populationList, individual):
    for other in populationList:
        if (other.currMapPosition == individual.currMapPosition):
            return False
    return True

def createMapFreeSpaceList(mapSizeX, mapSizeY):
    mapFreeSpaceList = []
    mapSizeY -= 1
    while (mapSizeY >= 0):
        tmpSizeX = mapSizeX - 1
        while (tmpSizeX >= 0):
            freePos = [mapSizeY, tmpSizeX]
            mapFreeSpaceList.append(freePos)
            tmpSizeX -= 1
        mapSizeY -= 1
    return mapFreeSpaceList

def spawnNewGeneration(populationNb, mapSizeX, mapSizeY, generationLifeSpan,
                       parentGeneration, currentGeneration, mutationProb):
    populationList = []
    mapFreeSpaceList = createMapFreeSpaceList(mapSizeX, mapSizeY)
    if (parentGeneration is None):
        while (populationNb > 0):
            while True:
                individual = Individual(mapSizeX, mapSizeY, 0,
                                        generationLifeSpan, populationNb,
                                        mapFreeSpaceList)
                mapFreeSpaceList.remove(individual.mapPosition[0])
                populationList.append(individual)
                populationNb -= 1
                if (len(mapFreeSpaceList) == 0):
                    return populationList
                break
    elif (parentGeneration is not None):
        newPopulationNb = 0
        alreadyReproduced = []
        survivors = 0
        while (survivors < len(parentGeneration)):
            if (parentGeneration[survivors] not in alreadyReproduced):
                birthParentNb = random.randint(0, 1)
                if (birthParentNb == 0
                    or parentGeneration[survivors].reproductionPartner not in parentGeneration):
                    parent = parentGeneration[survivors]
                    partner = parentGeneration[survivors].reproductionPartner
                elif (birthParentNb == 1):
                    parent = parentGeneration[survivors].reproductionPartner
                    partner = parentGeneration[survivors]
                childrenNb = parent.genePool.fertility
                while (childrenNb > 0):
                    individual = Child(parent, partner, mapSizeX, mapSizeY,
                                       currentGeneration, generationLifeSpan,
                                       newPopulationNb, mutationProb,
                                       mapFreeSpaceList)
                    mapFreeSpaceList.remove(individual.mapPosition[0])
                    populationList.append(individual)
                    newPopulationNb += 1
                    childrenNb -= 1
                    if (len(mapFreeSpaceList) == 0):
                        print("return ici")
                        return populationList
                alreadyReproduced.append(parent)
                alreadyReproduced.append(partner)
            survivors += 1

    return populationList


def runCurrentGenerationLife(populationList, generationLifeSpan,
                             mapRepresentation, foodList,
                             mapSizeX, mapSizeY):
    loopIndex = 0
    while (loopIndex < generationLifeSpan):
        initialFoodList = foodList[loopIndex][:]
        if (loopIndex > 0):
            for individual in populationList:
                if (individual.hasEaten == False
                        or individual.hasReproduced == False):
                    individual = setIndividualCurrentGoal(individual,
                                                              mapRepresentation,
                                                              populationList,
                                                              mapSizeX,
                                                              mapSizeY)
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
                individual.registerPrintingValuesHistory(loopIndex)
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
        if (partner.currMapPosition == targetCoord
            and checkIfTargetHasReproduced(partner.currMapPosition,
                                           populationList)):
            partner.reproduces(individual, loopIndex)
            if (partner.currentGoal == "reproduction"):
                partner.currentGoal = "none"
            return partner

def scanAdjacentTilesForTarget(currPosition, targetName, mapRepresentation):
    mapSizeY = len(mapRepresentation)
    mapSizeX = len(mapRepresentation[0])

    startY = currPosition[0]
    if (currPosition[0] - 1 >= 0):
        startY = currPosition[0] - 1
    endY = currPosition[0]
    if (currPosition[0] + 1 < mapSizeY):
        endY = currPosition[0] + 1
    startX = currPosition[1]
    if (currPosition[1] - 1 >= 0):
        startX = currPosition[1] - 1
    endX = currPosition[1]
    if (currPosition[1] + 1 < mapSizeX):
        endX = currPosition[1] + 1

    while (startY <= endY):
        loopStartX = startX
        while (loopStartX <= endX):
            if (mapRepresentation[startY][loopStartX] == targetName
                and (loopStartX != currPosition[1] or startY != currPosition[0])):
                return ([startY, loopStartX])
            loopStartX += 1
        startY += 1
    return None

def individualMoveToCurrentGoal(individual, mapRepresentation, populationList):
    # set diagonal movements
    targetPos = individual.currGoalPos
    currPos = individual.currMapPosition
    movementPool = individual.genePool.movement
    newMovement = random.choice(individual.genePool.movement)
    if ("diagUpLeft" in movementPool and targetPos[0] < currPos[0]
            and targetPos[1] < currPos[1]):
        newMovement = "diagUpLeft"
    elif ("diagUpRight" in movementPool and targetPos[0] < currPos[0]
            and targetPos[1] > currPos[1]):
        newMovement = "diagUpRight"
    elif ("diagDownLeft" in movementPool and targetPos[0] > currPos[0]
            and targetPos[1] < currPos[1]):
        newMovement = "diagDownLeft"
    elif ("diagDownRight" in movementPool and targetPos[0] > currPos[0]
            and targetPos[1] > currPos[1]):

        newMovement = "diagDownRight"
    elif ("down" in movementPool and targetPos[0] > currPos[0]):
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

def searchingForReproductionTarget(individual, mapRepresentation,
                                             populationList, mapSizeX, mapSizeY):
    reproductionTargetPos = scanForTargetOnMap(individual,
                                               individual.genePool.reproductionRadar,
                                               "individual",
                                               mapRepresentation,
                                               populationList,
                                               mapSizeX,
                                               mapSizeY)
    reproductionTargetPos = checkIfTargetIsReachable(individual,
                                                     reproductionTargetPos)
    if (reproductionTargetPos is not None):
        individual.setCurrentGoal("reproduction", reproductionTargetPos)
    return reproductionTargetPos

def searchingForFoodTarget(individual, mapRepresentation, populationList,
                           mapSizeX, mapSizeY):
    foodTargetPos = scanForTargetOnMap(individual,
                                       individual.genePool.foodRadar,
                                       "food",
                                       mapRepresentation,
                                       populationList,
                                       mapSizeX,
                                       mapSizeY)
    foodTargetPos = checkIfTargetIsReachable(individual,foodTargetPos)
    if (foodTargetPos is not None):
        individual.setCurrentGoal("food", foodTargetPos)
    return foodTargetPos

def setIndividualCurrentGoal(individual, mapRepresentation, populationList,
                             mapSizeX, mapSizeY):
    partnerFound = None
    foodFound = None
    if ((individual.hasEaten is True or individual.genePool.preference >= 5)
         and individual.hasReproduced is False):
            partnerFound = searchingForReproductionTarget(individual,
                           mapRepresentation, populationList, mapSizeX, mapSizeY)
            if (partnerFound is None and individual.hasEaten is False):
                foodFound = searchingForFoodTarget(individual, mapRepresentation,
                            populationList, mapSizeX, mapSizeY)
    else:
        if (individual.hasEaten is False):
            foodFound = searchingForFoodTarget(individual, mapRepresentation,
                            populationList, mapSizeX, mapSizeY)
        if (foodFound is None and individual.hasReproduced is False):
            partnerFound = searchingForReproductionTarget(individual,
                           mapRepresentation, populationList, mapSizeX, mapSizeY)
    return individual

def checkIfTargetIsReachable(individual, targetPos):
    if (targetPos):
        currPos = individual.currMapPosition
        if (abs(targetPos[0] - currPos[0]) < 2
                and abs(targetPos[1] - currPos[1]) < 2):
            return targetPos
        movementPool = individual.genePool.movement
        if (targetPos[0] > currPos[0] and "diagDownLeft" not in movementPool
                and "diagDownRight" not in movementPool
                and "down" not in movementPool):
            return None
        if (targetPos[0] < currPos[0] and "diagUpLeft" not in movementPool
                and "diagUpRight" not in movementPool
                and "up" not in movementPool):
            return None
        if (targetPos[1] < currPos[1] and "diagUpLeft" not in movementPool
                and "diagDownLeft" not in movementPool
                and "left" not in movementPool):
            return None
        if (targetPos[1] > currPos[1] and "diagUpRight" not in movementPool
                and "diagDownRight" not in movementPool
                and "right" not in movementPool):
            return None
        return targetPos
    return None

def scanForTargetOnMap(individual, geneRadar, targetCode, mapRepresentation,
                       populationList, mapSizeX, mapSizeY):
    if (geneRadar > 0):
        for distance in range(1, geneRadar + 1):
            for coordX in range(-distance, distance + 1):
                for coordY in range(-distance, distance + 1):
                    if (checkIfTargetPositionIsValid(individual, coordX,
                                                     coordY, mapSizeX,
                                                     mapSizeY)):
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
    target = [individual for individual in populationList if individual.currMapPosition == targetCoord]
    if (target is not None):
        return True
    # for target in populationList:
    #     if (target.currMapPosition == targetCoord):
    #         if (target.hasReproduced is False):
    #             return True
    return False


def checkIfTargetPositionIsValid(individual, coordX, coordY,
                                 mapSizeX, mapSizeY):
    if (coordX == 0 and coordY == 0):
        return False
    if (individual.currMapPosition[0] + coordY > mapSizeY - 1
            or individual.currMapPosition[1] + coordX > mapSizeX - 1):
        return False
    return True

def removeAllUnsuccessfullIndividuals(populationList):
    successfullPopulationList = []
    for individual in populationList:
        if (individual.hasEaten is True and individual.hasReproduced is True):
            successfullPopulationList.append(individual)
    return successfullPopulationList
