import random
from .genePool import GenePool


class Individual:

    def __init__(self, mainData, applicationGUI, mapFreeSpaceList, spawnRule):
        self.mapPosition = []
        initMapPos = self.__determineMapPositionFromSpawnRule(mainData,
                                                    applicationGUI, spawnRule,
                                                    mapFreeSpaceList)
        self.mapPosition.append([initMapPos[0], initMapPos[1]])
        self.genePool = GenePool(None, None, None)
        self.parents = None
        self.setStarterBasicAttributes(0, mainData.generationLifeSpan,
                                       mainData.populationNb)

    def __determineMapPositionFromSpawnRule(self, mainData, applicationGUI,
                                            spawnRule, mapFreeSpaceList):
        initMapPos = []
        if (spawnRule == "paint"):
            initMapPos = self.__getIndividualPosFromMap(mainData, applicationGUI)
        elif (spawnRule == "random"):
            initMapPos = random.choice(mapFreeSpaceList)
        return initMapPos



    def __getIndividualPosFromMap(self, mainData, applicationGUI):
        currY = 0
        spottedPopNb = 0
        while (currY < applicationGUI.mapSizeY):
            currX = 0
            while (currX < applicationGUI.mapSizeX):
                if (mainData.mapRepresentation[currY][currX] == "population"):
                    spottedPopNb += 1
                    if (spottedPopNb == mainData.populationNb):
                        return ([currY, currX])
                currX += 1
            currY += 1


    def setStarterBasicAttributes(self, generation, generationLifeSpan,
            populationNb):
        self.currMapPosition = self.mapPosition[len(self.mapPosition) - 1][:]
        self.generation = generation
        self.hasEaten = False
        self.hasEatenLoop = generationLifeSpan + 1
        self.hasReproduced = False
        self.escapedDanger = False
        self.hasReproducedLoop = generationLifeSpan + 1
        self.currentGoal = "none"
        self.currGoalPos = "none"
        self.currentGoalHistory = []
        self.currGoalPosHistory = []
        self.movementHistory = []
        self.name = str(generation) + "-" + str(populationNb)

    def eats(self, currentLoop):
        self.hasEaten = True
        self.hasEatenLoop = currentLoop
        self.setCurrentGoal("none", None)

    def reproduces(self, partner, currentLoop):
        self.hasReproduced = True
        self.hasReproducedLoop = currentLoop
        self.reproductionPartner = partner

    def setCurrentGoal(self, currentGoal, goalPos):
        self.currentGoal = currentGoal
        self.currGoalPos = goalPos

    def registerPrintingValuesHistory(self, loopIndex):
        self.currentGoalHistory.append(self.currentGoal)
        self.currGoalPosHistory.append(self.currGoalPos)

    def setCurrentMovement(self, direction, mapRepresentation, populationList):
        self.movementHistory.append(direction)
        self.__checkCoordIsAvailable(mapRepresentation, direction,
                populationList)

    def checkPopulationListNoCoordDoublon(self, populationList, currPosition):
        for individual in populationList:
            if (individual.currMapPosition == currPosition):
                return False
        return True

    def __checkCoordIsAvailable(self, mapRepresentation, direction,
            populationList):
        currPosition = self.currMapPosition[:]
        if (direction == "up" or "Up" in direction):
            currPosition[0] -= 1
        elif (direction == "down" or "Down" in direction):
            currPosition[0] += 1
        if (direction == "left" or "Left" in direction):
            currPosition[1] -= 1
        elif (direction == "right" or "Right" in direction):
            currPosition[1] += 1
        mapSizeY = len(mapRepresentation) - 1
        mapSizeX = len(mapRepresentation[0]) - 1
        if (currPosition == self.currMapPosition
                or (currPosition[0] <= mapSizeY and currPosition[1] <= mapSizeX
                    and currPosition[0] >= 0 and currPosition[1] >= 0
                    and mapRepresentation[currPosition[0]][currPosition[1]] == "empty"
                    and self.checkPopulationListNoCoordDoublon(populationList,
                        currPosition))):
            self.mapPosition.append(currPosition[:])
            self.currMapPosition = currPosition
        else:
            self.mapPosition.append(self.currMapPosition[:])
