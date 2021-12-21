import random
from .fixedGenePool import FixedGenePool

class FixedChild:

    def __init__(self, generation, generationLifeSpan, populationNb, mutationProb,
                 mapFreeSpaceList, AttributesList):
        self.mapPosition = []
        initMapPos = random.choice(mapFreeSpaceList)
        self.mapPosition.append([initMapPos[0], initMapPos[1]])
        self.genePool = FixedGenePool(AttributesList)


