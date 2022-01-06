import random
from .individual import Individual
from .fixedGenePool import FixedGenePool

class FixedChild(Individual):

    def __init__(self, mainData, populationNb, AttributesList, mapFreeSpaceList):
        generation = mainData.generationLoop
        generationLifeSpan = mainData.generationLifeSpan
        mutationProb = mainData.mutationProb
        self.mapPosition = []

        initMapPos = mainData.fixedPopulationPos[populationNb]
        self.mapPosition.append([initMapPos[0], initMapPos[1]])
        self.genePool = FixedGenePool(AttributesList.newGenerationAttributesList,
                                      mutationProb)
        self.parents = None
        self.setStarterBasicAttributes(generation, generationLifeSpan, populationNb)


