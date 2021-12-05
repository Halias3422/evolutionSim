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

    def __init__(self, parent):
        self.__initGeneLevels(parent)
        self.__initMovementGene(parent)
        self.__initDangerRadarGene(parent)
        self.__initFoodRadarGene(parent)
        self.__initReproductionRadarGene(parent)
        self.__initFertilityGene(parent)
        self.__initPreferenceGene(parent)
        self.__initFearGene(parent)

    def __initGeneLevels(self, parent):
        if (parent is None):
            self.geneLevels = {
                    "movement": 1,
                    "dangerRadar": 1,
                    "foodRadar": 1,
                    "reproductionRadar": 1,
                    "fertility": 1}

    def __initMovementGene(self, parent):
        if (parent is None):
            self.movement = []
            self.movement.append(self.directions[random.randint(0, 3)])
            self.movement.append("none")

    def __initDangerRadarGene(self, parent):
        if (parent is None):
            self.dangerRadar = random.randint(1, 2)

    def __initFoodRadarGene(self, parent):
        if (parent is None):
            self.foodRadar = random.randint(1, 2)

    def __initReproductionRadarGene(self, parent):
        if (parent is None):
            self.reproductionRadar = random.randint(1, 2)

    def __initFertilityGene(self, parent):
        if (parent is None):
            self.fertility = random.randint(1, 2)

    def __initPreferenceGene(self, parent):
        if (parent is None):
            self.preference = random.randint(0, 10)

    def __initFearGene(self, parent):
        if (parent is None):
            self.fear = random.randint(-10, 10)
