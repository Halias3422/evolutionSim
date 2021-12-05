import random
from .genePool import GenePool


class Individual:

    def __init__(self, mapSizeX, mapSizeY, generation):
        self.mapPosition = [random.randint(0, mapSizeY - 1),
                            random.randint(0, mapSizeX - 1)]
        self.generation = generation
        if (generation == 0):
            self.genePool = GenePool(None)
        self.hasEaten = False
        self.hasReproduced = False
        self.currentGoal = "none"

    def eats(self):
        self.hasEaten = True

    def reproduces(self, partner):
        self.hasReproduced = True
        self.reproductionPartner = partner

    def setCurrentGoal(self, currentGoal, goalPos):
        self.currentGoal = currentGoal
        self.currGoalPos = goalPos
