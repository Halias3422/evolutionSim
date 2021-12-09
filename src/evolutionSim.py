from gui.guiWindow import initGUIApplication
from gui.guiWindow import createGUImap
from population.population import spawnNewGeneration
from population.population import runCurrentGenerationLife
from population.population import removeAllUnsuccessfullIndividuals
from environment.food import spawnGenerationFood
from debug.print import *
from environment.mapRepresentation import *
from dataCollection.dataCollection import DataCollection

# populationNb = 100
winWidth = 1500
winHeight = 750
# mapSizeX = 50
# mapSizeY = 50
# generationLifeSpan = 200
# foodNb = populationNb
# foodVariation = 0

def runGenerationsLife():
    #init Run Variables
    dataCollection = []
    populationNb = int(applicationGUI.txtPopulationSize.get())
    mapSizeX = int(applicationGUI.txtMapSize.get())
    mapSizeY = int(applicationGUI.txtMapSize.get())
    generationLifeSpan = int(applicationGUI.txtGenerationLifeSpan.get())
    generationsNb = int(applicationGUI.txtGenerationNb.get())
    foodNb = int(applicationGUI.txtFoodNb.get())
    foodVariation = int(applicationGUI.txtFoodVariation.get())
    print("toujours la")
    createGUImap(applicationGUI, mapSizeX, mapSizeY)

    mapRepresentation = createMapRepresentation(mapSizeX, mapSizeY)
    populationList = spawnNewGeneration(populationNb, mapSizeX, mapSizeY,
                                        generationLifeSpan, None)
    mapRepresentation = addPopulationListToMapRepresentation(populationList,
                                                             mapRepresentation)

    foodList = []
    foodList.append(spawnGenerationFood(foodNb, foodVariation, applicationGUI.mapSizeX,
                                   applicationGUI.mapSizeY, mapRepresentation))
    mapRepresentation = addFoodListToMapRepresentation(foodList[0], mapRepresentation)

    populationList = runCurrentGenerationLife(populationList, generationLifeSpan,
                                              mapRepresentation, foodList)

    dataCollection.append(DataCollection(populationList))
    printDataCollectionForCurrentGeneration(dataCollection[0])
    applicationGUI.printGenerationLifeSpanFrameByFrame(populationList, foodList,
                                        generationLifeSpan)
    populationList = removeAllUnsuccessfullIndividuals(populationList)


# Initiate GUI components
print("init")
applicationGUI = initGUIApplication(winWidth, winHeight, runGenerationsLife)
print("apres init")
applicationGUI.mainWindow.mainloop()
