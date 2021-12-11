import random
from .genePool import GenePool


class Individual:

    def __init__(self, mapSizeX, mapSizeY, generation, generationLifeSpan,
            populationNb):
        self.mapPosition = []
        self.mapPosition.append([random.randint(0, mapSizeY - 1),
            random.randint(0, mapSizeX - 1)])
        self.genePool = GenePool(None, None, None)
        self.parents = None
        self.setStarterBasicAttributes(generation, generationLifeSpan, populationNb)


    def setStarterBasicAttributes(self, generation, generationLifeSpan,
            populationNb):
        self.currMapPosition = self.mapPosition[len(self.mapPosition) - 1][:]
        self.generation = generation
        self.hasEaten = False
        self.hasEatenLoop = generationLifeSpan + 1
        self.hasReproduced = False
        self.hasReproducedLoop = generationLifeSpan + 1
        self.currentGoal = "none"
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
