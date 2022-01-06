import random

class FixedGenePool:
    directions = ["up", "down", "left", "right", "diagUpLeft", "diagUpRight",
                  "diagDownLeft", "diagDownRight"]
    geneLevels = [["movement", 1],
                  ["dangerRadar", 1],
                  ["foodRadar", 1],
                  ["reproductionRadar", 1],
                  ["fertility", 0]]
    mutatedGene = None

    def __init__(self, attributesList, mutationProb):
        self.__initGeneLevels(attributesList, mutationProb)
        self.__registerGeneLevels()
        self.__initMovementGene(attributesList)
        self.__initPreferenceGene(attributesList)

    def __registerGeneLevels(self):
        self.movement = self.geneLevels["movement"]
        self.dangerRadar = self.geneLevels["dangerRadar"]
        self.foodRadar = self.geneLevels["foodRadar"]
        self.reproductionRadar = self.geneLevels["reproductionRadar"]
        self.fertility = 0


    def __initMovementGene(self, attributesList):
        self.movement = []
        movementLevel = self.geneLevels["movement"]
        if (self.mutatedGene == "movement"):
            movementLevel -= 1
        while (movementLevel > 0):
            self.movement.append(self.__getRandomValueFromAttributesList(\
                    attributesList, "direction"))
            movementLevel -= 1
        if (self.mutatedGene == "movement"):
            self.__mutationAddNewMovement()
        self.movement.append("none")

    def __mutationAddNewMovement(self):
        while True:
            newMovement = self.directions[random.randint(0, len(self.directions) - 1)]
            if (newMovement not in self.movement):
                self.movement.append(newMovement)
                return

    def __initGeneLevels(self, attributesList, mutationProb):
        self.geneLevels = {
            "movement": int(self.__getRandomValueFromAttributesList(\
                    attributesList["geneLevels"], "movement")),
            "dangerRadar": int(self.__getRandomValueFromAttributesList(\
                    attributesList["geneLevels"], "dangerRadar")),
            "foodRadar": int(self.__getRandomValueFromAttributesList(\
                    attributesList["geneLevels"], "foodRadar")),
            "reproductionRadar": int(self.__getRandomValueFromAttributesList(\
                    attributesList["geneLevels"], "reproductionRadar")),
                }
        if (mutationProb is not None and random.randint(0, 100) <= mutationProb):
            self.__mutateRandomGene(attributesList)

    def __mutateRandomGene(self, attributesList):
        geneChoice, genValue = random.choice(list(attributesList["geneLevels"].items()))
        self.geneLevels[geneChoice] += 1
        self.mutatedGene = geneChoice
        self.__checkForGeneMaxLevel()

    def __checkForGeneMaxLevel(self):
        if (self.geneLevels["movement"] > 8):
            self.geneLevels["movement"] = 8
        if (self.geneLevels["dangerRadar"] > 10):
            self.geneLevels["dangerRadar"] = 10
        if (self.geneLevels["foodRadar"] > 10):
            self.geneLevels["foodRadar"] = 10
        if (self.geneLevels["reproductionRadar"] > 10):
            self.geneLevels["reproductionRadar"] = 10

    def __initPreferenceGene(self, attributesList):
        self.preference = int(self.__getRandomValueFromAttributesList(attributesList,
                                                                  "preference"))


    def __getRandomValueFromAttributesList(self, attributesList, geneKey):
        chosenValue = 0
        loopIndex = 0
        while (chosenValue == 0):
            chosenKey, chosenValue = random.choice(list(attributesList\
                    [geneKey].items()))
            if (chosenValue > 0):
                attributesList[geneKey][chosenKey] -= 1
                return chosenKey
            loopIndex += 1
            if (loopIndex > 10
                    and self.__checkIfAttributeListKeyIsEmpty(attributesList\
                            [geneKey]) is True):
                return 1
        return 1

    def __checkIfAttributeListKeyIsEmpty(self, attributeList):
        allValues = list(attributeList.values())
        index = 0
        while (index < len(allValues)):
            if (allValues[index] != 0):
                return False
            index += 1
        return True


