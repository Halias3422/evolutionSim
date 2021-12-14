from .individual import Individual
from .genePool import GenePool
import random

class Child(Individual):
    pass

    def __init__(self, parent, parentPartner, mapSizeX, mapSizeY, generation,
                 generationLifeSpan, populationNb, mutationProb, mapFreeSpaceList):
        self.mapPosition = []
        initMapPos = random.choice(mapFreeSpaceList)
        self.mapPosition.append([initMapPos[0], initMapPos[1]])
        self.genePool = GenePool(parent, parentPartner, mutationProb)
        self.parents = [parent, parentPartner]
        self.setStarterBasicAttributes(generation, generationLifeSpan, populationNb)
