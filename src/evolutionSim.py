from gui.guiWindow import initGUIApplication
from gui.guiWindow import createGUImap
from population.population import spawnNewGeneration
from population.population import runCurrentGenerationLife
from population.population import removeAllUnsuccessfullIndividuals
from environment.food import spawnGenerationFood
from debug.print import *
from environment.mapRepresentation import *
from dataCollection.dataCollection import DataCollection

import cProfile

# populationNb = 100
winWidth = 1800
winHeight = 1000
# mapSizeX = 50
# mapSizeY = 50
# generationLifeSpan = 200
# foodNb = populationNb
# foodVariation = 0

def runGenerationsLife(applicationGUI, event=None):
    #init Run Variables
    dataCollection = []
    # populationNb = 500
    # mapSizeX = 50
    # mapSizeY = 50
    # generationLifeSpan = 100
    # generationsNb = 20
    # foodNb = 500
    # foodVariation = 0
    # parentGeneration = None
    # mutationProb = 100

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
        foodList.append(spawnGenerationFood(foodNb, foodVariation, mapSizeX,
                                            mapSizeY, mapRepresentation))
        mapRepresentation = addFoodListToMapRepresentation(foodList[0], mapRepresentation)

        populationList = runCurrentGenerationLife(populationList, generationLifeSpan,
                                                  mapRepresentation, foodList,
                                                  mapSizeX, mapSizeY)
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


# cProfile.run('runGenerationsLife()', 'profile.prof')
# Initiate GUI components
def main():
    print("TOTO")
    applicationGUI = initGUIApplication(winWidth, winHeight, runGenerationsLife)
    applicationGUI.mainWindow.mainloop()

if (__name__ == "__main__"):
    print("toto")
    main()

