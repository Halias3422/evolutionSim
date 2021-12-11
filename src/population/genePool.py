import random


class GenePool:
    directions = ["up", "down", "left", "right", "diagUpLeft", "diagUpRight",
                  "diagDownLeft", "diagDownRight"]
    geneLevels = [["movement", 1],
                  ["dangerRadar", 1],
                  ["foodRadar", 1],
                  ["reproductionRadar", 1],
                  ["fertility", 1]]

    # avalaible Genes :
    #     movement(starts with one of the first four + no movement)
    #            - 8 directions + no movement
    #     dangerRadar(starts between 1 and 2) - from 1 to 10
    #     foodRadar(starts between 1 and 2) - from 1 to 10
    #     reproductionRadar(starts between 1 and 2) - from 1 to 10
    #     fertility(starts between 1 and 2) - from 1 to 7
    #     preference - from 0 (food) to 10 (reproduction)
    #     fear - from -10 to 10

    def __init__(self, parent, parentPartner, mutationProb):
        self.__initGeneLevels(parent, parentPartner, mutationProb)
        self.__initMovementGene(self.__randParent(parent, parentPartner))
        self.__initDangerRadarGene(self.__randParent(parent, parentPartner))
        self.__initFoodRadarGene(self.__randParent(parent, parentPartner))
        self.__initReproductionRadarGene(self.__randParent(parent, parentPartner))
        self.__initFertilityGene(self.__randParent(parent, parentPartner))
        self.__initPreferenceGene(self.__randParent(parent, parentPartner))
        self.__initFearGene(self.__randParent(parent, parentPartner))

    def __randParent(self, parent, parentPartner):
        if (random.randint(0, 1) == 0):
            return parent
        else: return parentPartner

    def __checkForGeneMaxLevel(self):
        if (self.geneLevels["movement"] > 8):
            self.geneLevels["movement"] = 8
        if (self.geneLevels["dangerRadar"] > 10):
            self.geneLevels["dangerRadar"] = 10
        if (self.geneLevels["foodRadar"] > 10):
            self.geneLevels["foodRadar"] = 10
        if (self.geneLevels["reproductionRadar"] > 10):
            self.geneLevels["reproductionRadar"] = 10
        if (self.geneLevels["fertility"] > 7):
            self.geneLevels["fertility"] = 7

    def __initGeneLevels(self, parent, parentPartner, mutationProb):
        if (parent is None):
            self.geneLevels = {
                    "movement": 1,
                    "dangerRadar": 1,
                    "foodRadar": 1,
                    "reproductionRadar": 1,
                    "fertility": 1}
        else:
            self.geneLevels = {
                    "movement": int(self.__randParent(parent, parentPartner).genePool.geneLevels["movement"]),
                    "dangerRadar": int(self.__randParent(parent, parentPartner).genePool.geneLevels["dangerRadar"]),
                    "foodRadar": int(self.__randParent(parent, parentPartner).genePool.geneLevels["foodRadar"]),
                    "reproductionRadar": int(self.__randParent(parent, parentPartner).genePool.geneLevels["reproductionRadar"]),
                    "fertility": int(self.__randParent(parent, parentPartner).genePool.geneLevels["fertility"])}
            if (mutationProb is not None and random.randint(0, 100) <= mutationProb):
                self.geneLevels[random.choice(list(self.geneLevels))] += 1
                print("mutated Gene level!!")
                self.__checkForGeneMaxLevel()

    def __mutationAddNewMovement(self):
        while True:
            newMovement = self.directions[random.randint(0, len(self.directions) - 1)]
            if (newMovement not in self.movement):
                self.movement.append(newMovement)
                return

    def __initMovementGene(self, parent):
        self.movement = []
        if (parent is None):
            self.movement.append(self.directions[random.randint(0, 3)])
            self.movement.append("none")
        else:
            movementLevel = self.geneLevels["movement"]
            while (movementLevel > 0):
                while True:
                    if (len(self.movement) < len(parent.genePool.movement) - 1):
                        newMovement = parent.genePool.movement[random.randint(0, len(parent.genePool.movement) - 2)]
                        if (newMovement not in self.movement):
                            self.movement.append(newMovement)
                            movementLevel -= 1
                            break
                    else:
                        self.__mutationAddNewMovement()
                        movementLevel -= 1
                        break
            self.movement.append("none")

    def __initDangerRadarGene(self, parent):
        if (parent is None):
            self.dangerRadar = random.randint(1, 2)
        elif (parent.genePool.dangerRadar < 1 + self.geneLevels["dangerRadar"]):
            self.dangerRadar = random.randint(parent.genePool.dangerRadar,
                                              1 + self.geneLevels["dangerRadar"])
        else:
            self.dangerRadar = parent.genePool.dangerRadar

    def __initFoodRadarGene(self, parent):
        if (parent is None):
            self.foodRadar = random.randint(1, 2)
        elif (parent.genePool.foodRadar < 1 + self.geneLevels["foodRadar"]):
            self.foodRadar = random.randint(parent.genePool.foodRadar,
                                            1 + self.geneLevels["foodRadar"])
        else:
            self.foodRadar = parent.genePool.foodRadar

    def __initReproductionRadarGene(self, parent):
        if (parent is None):
            self.reproductionRadar = random.randint(1, 2)
        elif (parent.genePool.reproductionRadar <
              1 + self.geneLevels["reproductionRadar"]):
            self.reproductionRadar = random.randint(parent.genePool.reproductionRadar,
                                                    1 + self.geneLevels["reproductionRadar"])
        else:
            self.reproductionRadar = parent.genePool.reproductionRadar


    def __initFertilityGene(self, parent):
        if (parent is None):
            self.fertility = random.randint(1, 2)
        elif (parent.genePool.fertility < 1 + self.geneLevels["fertility"]):
            self.fertility = random.randint(parent.genePool.fertility,
                                            1 + self.geneLevels["fertility"])
        else:
            self.fertility = parent.genePool.fertility

    def __initPreferenceGene(self, parent):
        if (parent is None):
            self.preference = random.randint(0, 10)
        else:
            self.preference = parent.genePool.preference

    def __initFearGene(self, parent):
        if (parent is None):
            self.fear = random.randint(-10, 10)
        else:
            self.fear = parent.genePool.fear
