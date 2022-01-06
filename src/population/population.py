from .individual import Individual
from .child import Child
from environment.mapRepresentation import updateMapRepresentation
import random
from .newFixedGenerationAttributes import NewFixedGenerationAttributes
from .fixedChild import FixedChild

def checkIfCoordinateNotOccupied(populationList, individual):
    for other in populationList:
        if (other.currMapPosition == individual.currMapPosition):
            return False
    return True

def createMapFreeSpaceList(mainData):
    mapSizeX = mainData.mapSizeX
    mapSizeY = mainData.mapSizeY
    zonesMap = mainData.mapRepresentation
    mapFreeSpaceList = []
    mapSizeY -= 1
    while (mapSizeY >= 0):
        tmpSizeX = mapSizeX - 1
        while (tmpSizeX >= 0):
            if (zonesMap[mapSizeY][tmpSizeX] == "empty"):
                freePos = [mapSizeY, tmpSizeX]
                mapFreeSpaceList.append(freePos)
            tmpSizeX -= 1
        mapSizeY -= 1
    return mapFreeSpaceList

def spawnRunFirstGeneration(applicationGUI, mainData, mapFreeSpaceList):
    populationList = []
    while (mainData.populationNb > 0):
        while True:
            if (len(mapFreeSpaceList) == 0):
                return populationList
            individual = Individual(mainData, applicationGUI, mapFreeSpaceList,
                        applicationGUI.menus.mainMenu.optionPopulationGen.get())
            if (individual.mapPosition[0] in mapFreeSpaceList):
                mapFreeSpaceList.remove(individual.mapPosition[0])
            populationList.append(individual)
            mainData.populationNb -= 1
            if (mainData.populationReproductionGen == False):
                mainData.fixedPopulationPos.append(individual.mapPosition[0])
            break
    return populationList

def spawnNewGeneration(applicationGUI, mainData):
    populationList = []
    mapFreeSpaceList = createMapFreeSpaceList(mainData)
    if (mainData.parentGeneration is None):
        populationList = spawnRunFirstGeneration(applicationGUI, mainData,
                                                  mapFreeSpaceList)
    elif (mainData.parentGeneration is not None
            and mainData.populationReproductionGen == True):
        populationList = spawnNewGenerationChildrenRule(mainData, populationList,
                                                        mapFreeSpaceList)
    elif (mainData.parentGeneration is not None
            and mainData.populationReproductionGen == False):
        populationList = spawnNewGenerationFixedRule(mainData, populationList,
                                                     mapFreeSpaceList)

    return populationList

def spawnNewGenerationFixedRule(mainData, populationList, mapFreeSpaceList):
    newPopulationNb = 0
    newGenerationAttributesList = NewFixedGenerationAttributes(mainData)
    while (newPopulationNb < mainData.beginningPopulationNb):
        if (len(mapFreeSpaceList) == 0
                or newPopulationNb >= len(mainData.fixedPopulationPos)):
            break
        individual = FixedChild(mainData, newPopulationNb, newGenerationAttributesList,
                                mapFreeSpaceList)
        populationList.append(individual)
        newPopulationNb += 1
    return populationList


def spawnNewGenerationChildrenRule(mainData, populationList, mapFreeSpaceList):
    newPopulationNb = 0
    alreadyReproduced = []
    survivors = 0
    while (survivors < len(mainData.parentGeneration)):
        if (mainData.parentGeneration[survivors] not in alreadyReproduced):
            birthParentNb = random.randint(0, 1)
            if (birthParentNb == 0
                or mainData.parentGeneration[survivors].reproductionPartner not in mainData.parentGeneration):
                parent = mainData.parentGeneration[survivors]
                partner = mainData.parentGeneration[survivors].reproductionPartner
            elif (birthParentNb == 1):
                parent = mainData.parentGeneration[survivors].reproductionPartner
                partner = mainData.parentGeneration[survivors]
            childrenNb = parent.genePool.fertility
            while (childrenNb > 0):
                individual = Child(parent, partner, mainData.generationLoop,
                                   mainData.generationLifeSpan, newPopulationNb,
                                   mainData.mutationProb, mapFreeSpaceList)
                mapFreeSpaceList.remove(individual.mapPosition[0])
                populationList.append(individual)
                newPopulationNb += 1
                childrenNb -= 1
                if (len(mapFreeSpaceList) == 0):
                    return populationList
            alreadyReproduced.append(parent)
            alreadyReproduced.append(partner)
        survivors += 1
    return populationList

def runCurrentGenerationLife(populationList, mainData, mapRepresentation,
                             foodList):
    generationLifeSpan = mainData.generationLifeSpan
    mapSizeX = mainData.mapSizeX
    mapSizeY = mainData.mapSizeY
    loopIndex = 0
    currGenInfo = []
    while (loopIndex < generationLifeSpan):
        initialFoodList = foodList[loopIndex][:]
        populationInfo = {
                "hasEaten": 0,
                "hasReproduced": 0,
                "popNb": 0,
                }
        if (loopIndex > 0):
            for individual in populationList:
                individual = decideIndividualCurrentAction(individual, mapRepresentation,
                                              populationList, mapSizeX, mapSizeY,
                                              loopIndex, initialFoodList, mainData)
                populationInfo = fillPopulationInfo(individual, populationInfo)
        foodList.append(initialFoodList)
        mapRepresentation = updateMapRepresentation(mapRepresentation,
                                                    populationList, foodList,
                                                    loopIndex, mainData)
        populationInfo["popNb"] = len(populationList)
        currGenInfo.append(populationInfo)
        loopIndex += 1
    mainData.populationInfoPerLoop.append(currGenInfo)
    populationList = registerIndividualWhoEscapedDangerZone(populationList, mainData)
    return populationList

def individualIsInDangerZone(individual, mainData):
    if (mainData.dangerZoneMapRepresentation[individual.currMapPosition[0]]\
            [individual.currMapPosition[1]] == "danger"):
        return True
    return False

def individualGetOutOfDangerZone(individual, mainData, mapRepresentation):
    #find lower danger Lvl and check if can go there
    dangerLvlMap = mainData.dangerLevelMapRepresentation
    currY = individual.currMapPosition[0]
    currX = individual.currMapPosition[1]
    currDangerTileLvl = dangerLvlMap[currY][currX]
    amplitude = 1

    while (amplitude <= individual.genePool.dangerRadar + 1):
        checkY = currY - amplitude
        while (checkY <= currY + amplitude):
            checkX = currX - amplitude
            while (checkX <= currX + amplitude):
                if (checkY < mainData.mapSizeY and checkX < mainData.mapSizeX
                        and dangerLvlMap[checkY][checkX] < currDangerTileLvl
                        and mapRepresentation[checkY][checkX] == "empty"
                        and compareIndividualMovementPoolToTargetPos(individual,
                         ([checkY, checkX]), individual.currMapPosition) != None):
                    individual.setCurrentGoal("escape danger", [checkY, checkX])
                    return individual
                checkX += 1
            checkY += 1
        amplitude += 1
    return individual

def decideIndividualCurrentAction(individual, mapRepresentation, populationList,
                                  mapSizeX, mapSizeY, loopIndex, initialFoodList,
                                  mainData):
    if (individual.currentGoal == "escape danger"):
        individual.currentGoal = "none"
        individual.currGoalPos = "none"
    if (individual.hasEaten == False
            or individual.hasReproduced == False):
        individual = setIndividualCurrentGoal(individual,
                                                  mapRepresentation,
                                                  populationList,
                                                  mapSizeX,
                                                  mapSizeY)
    if (individual.currentGoal == "none"
            and individualIsInDangerZone(individual, mainData) is True):
        individual = individualGetOutOfDangerZone(individual, mainData,
                                                  mapRepresentation)
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
    return individual

def fillPopulationInfo(individual, populationInfo):
    if (individual.hasEaten):
        populationInfo["hasEaten"] += 1
    if (individual.hasReproduced):
        populationInfo["hasReproduced"] += 1
    return populationInfo

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

def compareIndividualMovementPoolToTargetPos(individual, targetPos, currPos):
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

def checkIfTargetIsReachable(individual, targetPos):
    if (targetPos):
        currPos = individual.currMapPosition
        if (abs(targetPos[0] - currPos[0]) < 2
                and abs(targetPos[1] - currPos[1]) < 2):
            return targetPos
        targetPos = compareIndividualMovementPoolToTargetPos(individual, targetPos,
                                                             currPos)
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

def registerIndividualWhoEscapedDangerZone(populationList, mainData):
    for individual in populationList:
        if (mainData.dangerZoneMapRepresentation[individual.mapPosition[-1][0]]\
                [individual.mapPosition[-1][1]] == "empty"):
            individual.escapedDanger = True
        else:
            individual.escapedDanger = False
    return populationList

def removeAllUnsuccessfullIndividuals(populationList, mainData):
    successfullPopulationList = []
    for individual in populationList:
        if (individual.hasEaten is True and individual.hasReproduced is True
                and individual.escapedDanger is True):
            successfullPopulationList.append(individual)
    return successfullPopulationList
