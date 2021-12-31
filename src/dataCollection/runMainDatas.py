from environment.mapRepresentation import createMapRepresentation

class RunMainDatas:

    def __init__(self, applicationGUI):
        self.beginningPopulationNb = int(applicationGUI.menus.mainMenu.txtPopulationSize.get())

        self.populationNb = int(applicationGUI.menus.mainMenu.txtPopulationSize.get())
        self.mapSizeX = int(applicationGUI.menus.mainMenu.txtMapSize.get())
        self.mapSizeY = int(applicationGUI.menus.mainMenu.txtMapSize.get())
        self.generationLifeSpan = int(applicationGUI.menus.mainMenu.txtGenerationLifeSpan.get())
        self.generationsNb = int(applicationGUI.menus.mainMenu.txtGenerationNb.get())
        self.foodNb = int(applicationGUI.menus.mainMenu.txtFoodNb.get())
        self.parentGeneration = None
        self.mutationProb = float(applicationGUI.menus.mainMenu.txtMutationProb.get())
        self.generationLoop = 0
        self.dataCollection = []
        self.allGenerationsPopulationList = []
        self.allGenerationsFoodList = []
        self.populationInfoPerLoop = []
        self.mapRepresentation = createMapRepresentation(self.mapSizeX, self.mapSizeY)

    def updateMapRepresentationWithZones(self, applicationGUI):
        self.mapRepresentation = applicationGUI.menus.dangerPaintingMenu.mapZonesRepresentation
        print(self.mapRepresentation)

