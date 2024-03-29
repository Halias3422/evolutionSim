from environment.mapRepresentation import createMapRepresentation

class RunMainDatas:

    def __init__(self, applicationGUI):
        mainMenu = applicationGUI.menus.mainMenu
        self.beginningPopulationNb = int(mainMenu.txtPopulationSize.get())

        self.populationNb = int(mainMenu.txtPopulationSize.get())
        self.mapSizeX = int(mainMenu.txtMapSize.get())
        self.mapSizeY = int(mainMenu.txtMapSize.get())
        self.generationLifeSpan = int(mainMenu.txtGenerationLifeSpan.get())
        self.generationsNb = int(mainMenu.txtGenerationNb.get())
        self.dangerNb = int(mainMenu.txtDangerNb.get())
        self.obstacleNb = int(mainMenu.txtObstacleNb.get())
        self.foodNb = int(mainMenu.txtFoodNb.get())
        self.parentGeneration = None
        self.mutationProb = float(mainMenu.txtMutationProb.get())
        self.generationLoop = 0
        self.dataCollection = []
        self.allGenerationsPopulationList = []
        self.allGenerationsFoodList = []
        self.obstacleList = []
        self.dangerList = []
        self.populationInfoPerLoop = []
        self.mapRepresentation = createMapRepresentation(self.mapSizeX, self.mapSizeY)
        self.dangerZoneMapRepresentation = self.mapRepresentation[:]
        self.dangerLevelsMapRepresentation = []
        self.zonesMapRepresentation = self.mapRepresentation[:]
        self.dangerGen = mainMenu.optionDangerGen.get()
        self.populationGen = mainMenu.optionPopulationGen.get()
        self.populationReproductionGen = mainMenu.optionPopulationReproduction.get()
        self.foodGen = mainMenu.optionFoodGen.get()
        self.obstacleGen = mainMenu.optionObstacleGen.get()
        self.reproductionToggle = mainMenu.optionReproductionGen.get()
        self.foodToggle = False
        if (self.foodGen == "disable"):
            self.foodToggle = True
        self.fixedPopulationPos = []

    def __initZonesMapsRepresentation(self, applicationGUI):
        self.zonesMapRepresentation = applicationGUI.menus.zonePaintingMenu.mapZonesRepresentation
        self.dangerZoneMapRepresentation = applicationGUI.menus.zonePaintingMenu.mapDangerZonesRepresentation

    def updateMainDataAfterPainting(self, applicationGUI, mainData):
        self.__initZonesMapsRepresentation(applicationGUI)
        mapSizeY = mainData.mapSizeY - 1
        mapSizeX = mainData.mapSizeX - 1
        zoneMap = mainData.zonesMapRepresentation
        dangerZoneMap = mainData.dangerZoneMapRepresentation
        environment = {
                "population": 0,
                "danger": 0,
                "food": 0,
                "obstacle": 0
                }
        while (mapSizeY >= 0):
            tmpSizeX = mapSizeX
            while (tmpSizeX >= 0):
                if (zoneMap[mapSizeY][tmpSizeX] == "population"):
                    environment["population"] += 1
                elif (zoneMap[mapSizeY][tmpSizeX] == "food"):
                    environment["food"] += 1
                elif (zoneMap[mapSizeY][tmpSizeX] == "obstacle"):
                    environment["obstacle"] += 1
                if (dangerZoneMap[mapSizeY][tmpSizeX] == "danger"):
                    environment["danger"] += 1
                tmpSizeX -= 1
            mapSizeY -= 1
        if (self.populationGen == "paint"):
            self.populationNb = environment["population"]
            self.beginningPopulationNb = environment["population"]
        if (self.dangerGen == "paint"):
            self.dangerNb = environment["danger"]
        if (self.foodGen == "paint"):
            self.foodNb = environment["food"]
        if (self.obstacleGen == "paint"):
            self.obstacleNb = environment["obstacle"]



