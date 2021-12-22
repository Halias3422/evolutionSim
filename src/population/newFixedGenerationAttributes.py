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
                },
            "preference": {"0": 0,"1": 0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,
                            "8":0, "9":0},
            "fear": {"-10": 0,"-9": 0,"-8": 0,"-7": 0,"-6": 0,"-5": 0,"-4": 0,
                     "-3": 0, "-2":0, "-1": 0,"0": 0,"1": 0,"2":0,"3":0,"4":0,
                     "5":0,"6":0,"7":0,"8":0, "9":0, "10":0},

            }
    def __init__(self, mainData):
        parentGeneration = mainData.parentGeneration
        for parent in parentGeneration:
            self.__updateDirectionAttribute(parent)
            self.__updateGeneLevelsAttribute(parent)
            self.__updatePreferenceAttribute(parent)
            self.__updateFearAttribute(parent)
        self.__calculateDirectionPercentageForNewGeneration(\
                mainData.beginningPopulationNb, parentGeneration)
        self.__calculateGeneLevelsPercentageForNewGeneration(\
                mainData.beginningPopulationNb, parentGeneration)
        self.__calculatePreferencePercentageForNewGeneration(\
                mainData.beginningPopulationNb, parentGeneration)
        self.__calculateFearPercentageForNewGeneration(\
                mainData.beginningPopulationNb, parentGeneration)

    def __calculatePreferencePercentageForNewGeneration(self, populationNb,
                                                        parentGeneration):
        parentGenLen = len(parentGeneration)
        preference = self.newGenerationAttributesList["preference"]
        self.__calculateSpecificGeneLevelAttribute(preference, parentGenLen,
                                                    populationNb)

    def __calculateFearPercentageForNewGeneration(self, populationNb,
                                                  parentGeneration):
        parentGenLen = len(parentGeneration)
        fear = self.newGenerationAttributesList["fear"]
        self.__calculateSpecificGeneLevelAttribute(fear, parentGenLen,
                                                   populationNb)


    def __calculateGeneLevelsPercentageForNewGeneration(self, populationNb,
                                                        parentGeneration):
        parentGenLen = len(parentGeneration)
        geneLevels = self.newGenerationAttributesList["geneLevels"]
        self.__calculateSpecificGeneLevelAttribute(geneLevels["movement"],
                                                   parentGenLen, populationNb)
        self.__calculateSpecificGeneLevelAttribute(geneLevels["dangerRadar"],
                                                   parentGenLen, populationNb)
        self.__calculateSpecificGeneLevelAttribute(geneLevels["foodRadar"],
                                                   parentGenLen, populationNb)
        self.__calculateSpecificGeneLevelAttribute(geneLevels["reproductionRadar"],
                                                   parentGenLen, populationNb)

    def __calculateSpecificGeneLevelAttribute(self, attribute, parentGenLen,
                                              populationNb):
        if ("-10" in attribute):
            attribute["-10"] = int(math.ceil(populationNb * (attribute["-10"] / parentGenLen)))
        if ("-9" in attribute):
            attribute["-9"] = int(math.ceil(populationNb * (attribute["-9"] / parentGenLen)))
        if ("-8" in attribute):
            attribute["-8"] = int(math.ceil(populationNb * (attribute["-8"] / parentGenLen)))
        if ("-7" in attribute):
            attribute["-7"] = int(math.ceil(populationNb * (attribute["-7"] / parentGenLen)))
        if ("-6" in attribute):
            attribute["-6"] = int(math.ceil(populationNb * (attribute["-6"] / parentGenLen)))
        if ("-5" in attribute):
            attribute["-5"] = int(math.ceil(populationNb * (attribute["-5"] / parentGenLen)))
        if ("-4" in attribute):
            attribute["-4"] = int(math.ceil(populationNb * (attribute["-4"] / parentGenLen)))
        if ("-3" in attribute):
            attribute["-3"] = int(math.ceil(populationNb * (attribute["-3"] / parentGenLen)))
        if ("-2" in attribute):
            attribute["-2"] = int(math.ceil(populationNb * (attribute["-2"] / parentGenLen)))
        if ("-1" in attribute):
            attribute["-1"] = int(math.ceil(populationNb * (attribute["-1"] / parentGenLen)))
        if ("0" in attribute):
            attribute["0"] = int(math.ceil(populationNb * (attribute["0"] / parentGenLen)))

        attribute["1"] = int(math.ceil(populationNb * (attribute["1"] / parentGenLen)))
        attribute["2"] = int(math.ceil(populationNb * (attribute["2"] / parentGenLen)))
        attribute["3"] = int(math.ceil(populationNb * (attribute["3"] / parentGenLen)))
        attribute["4"] = int(math.ceil(populationNb * (attribute["4"] / parentGenLen)))
        attribute["5"] = int(math.ceil(populationNb * (attribute["5"] / parentGenLen)))
        attribute["6"] = int(math.ceil(populationNb * (attribute["6"] / parentGenLen)))
        attribute["7"] = int(math.ceil(populationNb * (attribute["7"] / parentGenLen)))
        attribute["8"] = int(math.ceil(populationNb * (attribute["8"] / parentGenLen)))
        if ("9" in attribute):
            attribute["9"] = int(math.ceil(populationNb * (attribute["9"] / parentGenLen)))
        if ("10" in attribute):
            attribute["10"] = int(math.ceil(populationNb * (attribute["10"] / parentGenLen)))

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

    def __updatePreferenceAttribute(self, parent):
        self.newGenerationAttributesList["preference"][str(parent.genePool.preference)]\
            += 1

    def __updateFearAttribute(self, parent):
        self.newGenerationAttributesList["fear"][str(parent.genePool.fear)] += 1

    def __updateGeneLevelsAttribute(self, parent):
        self.newGenerationAttributesList["geneLevels"]["movement"][str(parent.genePool.geneLevels["movement"])] += 1
        self.newGenerationAttributesList["geneLevels"]["dangerRadar"]\
                [str(parent.genePool.geneLevels["dangerRadar"])] += 1
        self.newGenerationAttributesList["geneLevels"]["foodRadar"]\
                [str(parent.genePool.geneLevels["foodRadar"])] += 1
        self.newGenerationAttributesList["geneLevels"]["reproductionRadar"]\
                [str(parent.genePool.geneLevels["reproductionRadar"])] += 1

    def __updateDirectionAttribute(self, parent):
        index = 0
        while (index < len(parent.genePool.movement)):
            if (parent.genePool.movement[index] != "none"):
                self.newGenerationAttributesList["direction"]\
                [parent.genePool.movement[index]] += 1
            index += 1
