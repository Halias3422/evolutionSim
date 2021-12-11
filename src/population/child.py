from .individual import Individual
from .genePool import GenePool
import random

class Child(Individual):
    pass

    def __init__(self, parent, parentPartner, mapSizeX, mapSizeY, generation,
                   generationLifeSpan, populationNb, mutationProb):
        self.mapPosition = []
        if (parent.currMapPosition[1] - 1 >= 0):
            xOffsetLeft = 1
        else:
            xOffsetLeft = 0
        if (parent.currMapPosition[1] + 1 <= mapSizeX - 1):
            xOffsetRight = 1
        else:
            xOffsetRight = 0
        if (parent.currMapPosition[0] - 1 >= 0):
            yOffsetUp = 1
        else:
            yOffsetUp = 0
        if (parent.currMapPosition[0] + 1 <= mapSizeY - 1):
            yOffsetDown = 1
        else:
            yOffsetDown = 0
        self.mapPosition.append([random.randint(parent.currMapPosition[0] - yOffsetUp,
            parent.currMapPosition[0] + yOffsetDown),
            random.randint(parent.currMapPosition[1] - xOffsetLeft,
                parent.currMapPosition[1] + xOffsetRight)])
        self.genePool = GenePool(parent, parentPartner, mutationProb)
        self.parents = [parent, parentPartner]
        self.setStarterBasicAttributes(generation, generationLifeSpan, populationNb)
