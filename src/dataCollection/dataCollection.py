class DataCollection:

    def __init__(self, populationList):
        self.populationSize = len(populationList)
        self.hasReproducedNb = 0
        self.hasEatenNb = 0
        self.hasEscapedDangerNb = 0
        self.hasSurvived = 0
        for individual in populationList:
            if (individual.hasReproduced):
                self.hasReproducedNb += 1
            if (individual.hasEaten):
                self.hasEatenNb += 1
            if (individual.escapedDanger):
                self.hasEscapedDangerNb += 1
            if (individual.hasReproduced and individual.hasEaten
                    and individual.escapedDanger):
                self.hasSurvived += 1
