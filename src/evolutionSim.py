from gui.guiWindow import initGUIApplication
from population.population import spawnNewGeneration
from population.population import runCurrentGenerationLife
from population.population import removeAllUnsuccessfullIndividuals
from environment.food import spawnGenerationFood
from debug.print import *
from environment.mapRepresentation import *
from dataCollection.dataCollection import DataCollection
from dataCollection.runMainDatas import RunMainDatas
from gui.runResultDisplay import PrintRunResult

winWidth = 1800
winHeight = 1000

def runGenerationsLife(applicationGUI, event=None):
    mainData = RunMainDatas(applicationGUI)
    applicationGUI.defineMapSize(mainData.mapSizeX, mainData.mapSizeY)
    applicationGUI.menus.mainMenu.printLoadingInit(applicationGUI.mainWindow)
    while (mainData.generationLoop < mainData.generationsNb):
        mapRepresentation = createMapRepresentation(mainData.mapSizeX, mainData.mapSizeY)
        populationList = spawnCurrentLoopGeneration(mainData)
        mapRepresentation = addPopulationListToMapRepresentation(populationList,
                                                                 mapRepresentation)
        foodList = spawnCurrentLoopFood(mainData, mapRepresentation)
        mapRepresentation = addFoodListToMapRepresentation(foodList[0], mapRepresentation)
        populationList = storeCurrentLoopData(populationList, foodList, mainData,
                                              mapRepresentation)
        printDataCollectionForCurrentGeneration(mainData.dataCollection[mainData.generationLoop])
        mainData.parentGeneration = removeAllUnsuccessfullIndividuals(populationList)
        printLoadingStateToUI(mainData, applicationGUI, "running")
        mainData.generationLoop += 1
        if (checkIfThereAreSurvivors(mainData, mainData.parentGeneration, applicationGUI)
                is False):
            break
    PrintRunResult(mainData, applicationGUI)


def checkIfThereAreSurvivors(mainData, parentGeneration, applicationGUI):
    if (len(parentGeneration) == 0):
        print("No more individuals at Generation " +
                str(mainData.generationLoop) + ". Aborting...")
        mainData.generationsNb = mainData.generationLoop
        printLoadingStateToUI(mainData, applicationGUI, "done")
        return False
    return True

def printLoadingStateToUI(mainData, applicationGUI, currentState):
    if (currentState == "running"):
        applicationGUI.menus.mainMenu.printCurrentLoadingDatas(mainData.dataCollection[mainData.generationLoop],
                                                            mainData.generationLoop,
                                                            applicationGUI.mainWindow,
                                                            mainData.generationsNb)
    else:
        applicationGUI.menus.mainMenu.printCurrentLoadingDatas(None, 0, None, 0)

def spawnCurrentLoopFood(mainData, mapRepresentation):
    foodList = []
    foodList.append(spawnGenerationFood(mainData.foodNb, mainData.foodVariation,
                                        mainData.mapSizeX, mainData.mapSizeY,
                                        mapRepresentation))
    return foodList

def spawnCurrentLoopGeneration(mainData):
    populationList = spawnNewGeneration(mainData.populationNb, mainData.mapSizeX,
                                        mainData.mapSizeY, mainData.generationLifeSpan,
                                        mainData.parentGeneration, mainData.generationLoop,
                                        mainData.mutationProb)
    return populationList

def storeCurrentLoopData(populationList, foodList, mainData, mapRepresentation):
    populationList = runCurrentGenerationLife(populationList, mainData.generationLifeSpan,
                                              mapRepresentation, foodList,
                                              mainData.mapSizeX, mainData.mapSizeY)
    mainData.allGenerationsPopulationList.append(populationList)
    mainData.allGenerationsFoodList.append(foodList)
    mainData.dataCollection.append(DataCollection(populationList))
    return populationList


def main():
    applicationGUI = initGUIApplication(winWidth, winHeight, runGenerationsLife)
    applicationGUI.mainWindow.mainloop()

if (__name__ == "__main__"):
    main()

