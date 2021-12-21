import math

class NewFixedGenerationAttributes:
    newGenerationAttributesList = {
            "direction": {
                "up": 0,
                "down": 0,
                "left": 0,
                "right":0,
                "diagUpLeft": 0,
                "diagUpRight": 0,
                "diagDownLeft": 0,
                "diagDownRight": 0
                },
            "geneLevels": {
                "movement": {"1": 0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,
                    "8":0 },
                "dangerRadar": {"1": 0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,
                    "8":0,"9":0,"10":0},
                "foodRadar": {"1": 0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,
                    "8":0,"9":0,"10":0},
                "reproductionRadar": {"1": 0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,
                    "8":0,"9":0,"10":0}
                # "fertility": {"1": 0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,
                #     "8":0,"9":0,"10":0},
                }
            }
    def __init__(self, mainData):
        parentGeneration = mainData.parentGeneration
        for parent in parentGeneration:
            self.__updateDirectionAttribute(parent)
            self.__updateGeneLevelsAttribute(parent)
        self.__calculateDirectionPercentageForNewGeneration(mainData.beginningPopulationNb,
                                                            parentGeneration)
        #RESUME HERE ADD PERCENTAGE CALCULATION FOR GENELEVELS

    def __calculateDirectionPercentageForNewGeneration(self, populationNb,
                                                        parentGeneration):
        attribute = self.newGenerationAttributesList["direction"]
        parentGenLen = len(parentGeneration)
        attribute["up"] = int(math.ceil(populationNb * (attribute["up"] / parentGenLen)))
        attribute["down"] = int(math.ceil(populationNb * (attribute["down"] / parentGenLen)))
        attribute["left"] = int(math.ceil(populationNb * (attribute["left"] / parentGenLen)))
        attribute["right"] = int(math.ceil(populationNb * (attribute["right"] / parentGenLen)))
        attribute["diagUpLeft"] = int(math.ceil(populationNb * (attribute["diagUpLeft"]
            / parentGenLen)))
        attribute["diagUpRight"] = int(math.ceil(populationNb * (attribute["diagUpRight"]
            / parentGenLen)))
        attribute["diagDownLeft"] = int(math.ceil(populationNb * (attribute["diagDownLeft"]
            / parentGenLen)))
        attribute["diagDownRight"] = int(math.ceil(populationNb * (attribute["diagDownRight"]
            / parentGenLen)))

    def __updateGeneLevelsAttribute(self, parent):
        self.newGenerationAttributesList["geneLevels"]["movement"][str(parent.genePool.geneLevels["movement"])] += 1
        self.newGenerationAttributesList["geneLevels"]["dangerRadar"]\
                [str(parent.genePool.geneLevels["dangerRadar"])] += 1
        self.newGenerationAttributesList["geneLevels"]["foodRadar"]\
                [str(parent.genePool.geneLevels["foodRadar"])] += 1
        self.newGenerationAttributesList["geneLevels"]["reproductionRadar"]\
                [str(parent.genePool.geneLevels["reproductionRadar"])] += 1
        # self.newGenerationAttributesList["fertility"]\
        #         [str(parent.genePool.geneLevels["fertility"])] += 1

    def __updateDirectionAttribute(self, parent):
        index = 0
        while (index < len(parent.genePool.movement)):
            if (parent.genePool.movement[index] != "none"):
                self.newGenerationAttributesList["direction"]\
                [parent.genePool.movement[index]] += 1
            index += 1
