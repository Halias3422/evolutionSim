from gui.guiWindow import initGUIApplication
from gui.guiWindow import createGUImap
from population.population import spawnNewGeneration
from population.population import runCurrentGenerationLife
from population.population import removeAllUnsuccessfullIndividuals
from environment.food import spawnGenerationFood
from debug.print import *
from environment.mapRepresentation import *
from dataCollection.dataCollection import DataCollection

winWidth = 1800
winHeight = 1000

def runGenerationsLife(applicationGUI, event=None):
    #init Run Variables
    dataCollection = []
    populationNb = int(applicationGUI.menus.mainMenu.txtPopulationSize.get())
    mapSizeX = int(applicationGUI.menus.mainMenu.txtMapSize.get())
    mapSizeY = int(applicationGUI.menus.mainMenu.txtMapSize.get())
    generationLifeSpan = int(applicationGUI.menus.mainMenu.txtGenerationLifeSpan.get())
    generationsNb = int(applicationGUI.menus.mainMenu.txtGenerationNb.get())
    foodNb = int(applicationGUI.menus.mainMenu.txtFoodNb.get())
    foodVariation = int(applicationGUI.menus.mainMenu.txtFoodVariation.get())
    createGUImap(applicationGUI, mapSizeX, mapSizeY)
    parentGeneration = None
    mutationProb = float(applicationGUI.menus.mainMenu.txtMutationProb.get())
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
        applicationGUI.menus.mainMenu.printCurrentLoadingDatas(dataCollection[generationLoop], generationLoop, applicationGUI.mainWindow)
        generationLoop += 1
        if (len(parentGeneration) == 0):
            print("No more individuals at Generation " + str(generationLoop) + ". Aborting...")
            generationsNb = generationLoop
            break
    applicationGUI.printGenerationsLifeSpanFrameByFrame(allGenerationsPopulationList,
                                                        allGenerationsFoodList,
                                                        generationLifeSpan,
                                                        generationsNb)


def main():
    print("TOTO")
    applicationGUI = initGUIApplication(winWidth, winHeight, runGenerationsLife)
    applicationGUI.mainWindow.mainloop()

if (__name__ == "__main__"):
    print("toto")
    main()

