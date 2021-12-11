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

def runGenerationsLife(event=None):
    #init Run Variables
    dataCollection = []
    populationNb = int(applicationGUI.txtPopulationSize.get())
    mapSizeX = int(applicationGUI.txtMapSize.get())
    mapSizeY = int(applicationGUI.txtMapSize.get())
    generationLifeSpan = int(applicationGUI.txtGenerationLifeSpan.get())
    generationsNb = int(applicationGUI.txtGenerationNb.get())
    foodNb = int(applicationGUI.txtFoodNb.get())
    foodVariation = int(applicationGUI.txtFoodVariation.get())
    createGUImap(applicationGUI, mapSizeX, mapSizeY)
    parentGeneration = None
    mutationProb = float(applicationGUI.txtMutationProb.get())

    generationLoop = 0
    allGenerationsPopulationList = []
    allGenerationsFoodList = []
    while (generationLoop < generationsNb):
        mapRepresentation = createMapRepresentation(mapSizeX, mapSizeY)
        populationList = spawnNewGeneration(populationNb, mapSizeX, mapSizeY,
                                            generationLifeSpan, parentGeneration,
                                            generationLoop, mutationProb)
        mapRepresentation = addPopulationListToMapRepresentation(populationList,
                                                                 mapRepresentation)

        foodList = []
        foodList.append(spawnGenerationFood(foodNb, foodVariation, applicationGUI.mapSizeX,
                                       applicationGUI.mapSizeY, mapRepresentation))
        mapRepresentation = addFoodListToMapRepresentation(foodList[0], mapRepresentation)

        populationList = runCurrentGenerationLife(populationList, generationLifeSpan,
                                                  mapRepresentation, foodList)
        allGenerationsPopulationList.append(populationList)
        allGenerationsFoodList.append(foodList)
        dataCollection.append(DataCollection(populationList))
        printDataCollectionForCurrentGeneration(dataCollection[generationLoop])
        parentGeneration = removeAllUnsuccessfullIndividuals(populationList)
        generationLoop += 1
        if (len(parentGeneration) == 0):
            print("No more individuals at Generation " + str(generationLoop) + ". Aborting...")
            generationsNb = generationLoop
            break
    applicationGUI.printGenerationsLifeSpanFrameByFrame(allGenerationsPopulationList,
                                                        allGenerationsFoodList,
                                                        generationLifeSpan,
                                                        generationsNb)



# Initiate GUI components
applicationGUI = initGUIApplication(winWidth, winHeight, runGenerationsLife)
applicationGUI.mainWindow.mainloop()
