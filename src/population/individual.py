import random
from .genePool import GenePool


class Individual:

    def __init__(self, mapSizeX, mapSizeY, generation, generationLifeSpan,
                 populationNb):
        self.mapPosition = []
        self.mapPosition.append([random.randint(0, mapSizeY - 1),
                                random.randint(0, mapSizeX - 1)])
        self.currMapPosition = self.mapPosition[len(self.mapPosition) - 1][:]

        self.generation = generation
        if (generation == 0):
            self.genePool = GenePool(None)
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

    def setCurrentMovement(self, direction, mapRepresentation):
        self.movementHistory.append(direction)
        self.__checkCoordIsAvailable(mapRepresentation, direction)

    def __checkCoordIsAvailable(self, mapRepresentation, direction):
        currPosition = self.currMapPosition[:]
        if (direction == "up"):
            currPosition[0] -= 1
        elif (direction == "down"):
            currPosition[0] += 1
        if (direction == "left"):
            currPosition[1] -= 1
        elif (direction == "right"):
            currPosition[1] += 1
        mapSizeY = len(mapRepresentation) - 1
        mapSizeX = len(mapRepresentation[0]) - 1
        if (currPosition == self.currMapPosition
            or (currPosition[0] <= mapSizeY and currPosition[1] <= mapSizeX
                and currPosition[0] >= 0 and currPosition[1] >= 0
                and mapRepresentation[currPosition[0]][currPosition[1]] == "empty")):
            self.mapPosition.append(currPosition[:])
            self.currMapPosition = currPosition
        else:
            self.mapPosition.append(self.currMapPosition[:])
