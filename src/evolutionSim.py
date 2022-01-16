from gui.guiWindow import initGUIApplication
from population.population import spawnNewGeneration
from population.population import runCurrentGenerationLife
from population.population import removeAllUnsuccessfullIndividuals
from environment.food import spawnGenerationFood
from environment.food import getFoodListFromMapRepresentation
from debug.print import *
from environment.mapRepresentation import *
from dataCollection.dataCollection import DataCollection
from dataCollection.runMainDatas import RunMainDatas
from gui.runResultDisplay import PrintRunResult

winWidth = 1800
winHeight = 1000

def runGenerationsLife(applicationGUI, event=None):
    mainData = RunMainDatas(applicationGUI)
    handleMapZonePainting (applicationGUI, mainData)
    initApplicationState(applicationGUI, mainData)
    handleRandomZonesGeneration(applicationGUI, mainData)
    initialMapRepresentation = addZonesToMapRepresentation(mainData)
    while (mainData.generationLoop < mainData.generationsNb):
        mainData.mapRepresentation = copyInitialMapRepresentation(\
                                                        initialMapRepresentation,
                                                        mainData)
        populationList = spawnCurrentLoopGeneration(applicationGUI, mainData)
        mainData.mapRepresentation = addPopulationListToMapRepresentation(populationList,
                                                     mainData.mapRepresentation)
        foodList = spawnCurrentLoopFood(mainData, mainData.mapRepresentation)
        populationList = storeCurrentLoopData(populationList, foodList, mainData,
                                              mainData.mapRepresentation)
        mainData.parentGeneration = removeAllUnsuccessfullIndividuals(populationList,
                                                                      mainData)
        printLoadingStateToUI(mainData, applicationGUI, "running")
        mainData.generationLoop += 1
        if (checkIfThereAreSurvivors(mainData, mainData.parentGeneration, applicationGUI)
                is False):
            break
    PrintRunResult(mainData, applicationGUI)

def copyInitialMapRepresentation(initialMapRepresentation, mainData):
    newMap = createMapRepresentation(mainData.mapSizeX, mainData.mapSizeY)
    for y in range(0, mainData.mapSizeY):
        for x in range(0, mainData.mapSizeX):
            newMap[y][x] = initialMapRepresentation[y][x]
    return newMap

def handleRandomZonesGeneration(applicationGUI, mainData):
    mainMenu = applicationGUI.menus.mainMenu
    if (mainMenu.optionDangerGen.get() == "random"):
        mainData.dangerZoneMapRepresentation = generateDangerZoneMap(mainData)
    if (mainMenu.optionFoodGen.get() == "random"):
        mainData.zonesMapRepresentation = addRandomZoneToZoneMap(mainData, "food",
                                                             mainData.foodNb)
    if (mainMenu.optionObstacleGen.get() == "random"):
        mainData.zonesMapRepresentation = addRandomZoneToZoneMap(mainData, "obstacle",
                                                                 mainData.obstacleNb)
    mainData.dangerLevelMapRepresentation = generateDangerLevelMap(mainData,
                                                                   applicationGUI)

def initApplicationState(applicationGUI, mainData):
    applicationGUI.map.bind("<Button-1>", applicationGUI.focusOnMap())
    applicationGUI.mainWindow.focus_set()
    applicationGUI.defineMapSize(mainData.mapSizeX, mainData.mapSizeY)
    applicationGUI.menus.mainMenu.printLoadingInit(applicationGUI.mainWindow)

def handleMapZonePainting(applicationGUI, mainData):
    if (neededMapPainting(applicationGUI) is True):
        applicationGUI.map.delete("all")
        menus = applicationGUI.menus
        menus.createPaintingMenu(applicationGUI)
        menus.zonePaintingMenu.addZonesToMap(applicationGUI,
                                                                    mainData)
        mainData = mainData.updateMainDataAfterPainting(applicationGUI, mainData)
        menus.menusTabs.hide(menus.zonePaintingMenu.zonesPaintingFrame)
        applicationGUI.map.delete("all")


def neededMapPainting(applicationGUI):
    menu = applicationGUI.menus.mainMenu
    if (menu.optionPopulationGen.get() == "paint"):
        return True
    elif (menu.optionDangerGen.get() == "paint"):
        return True
    elif (menu.optionFoodGen.get() == "paint"):
        return True
    elif (menu.optionObstacleGen.get() == "paint"):
        return True
    return False

def checkIfThereAreSurvivors(mainData, parentGeneration, applicationGUI):
    if (len(parentGeneration) == 0):
        print("No more individuals at Generation " +
                str(mainData.generationLoop) + ". Aborting...")
        mainData.generationsNb = mainData.generationLoop
        printLoadingStateToUI(mainData, applicationGUI, "done")
        return False
    return True

def printLoadingStateToUI(mainData, applicationGUI, currentState):
    menus = applicationGUI.menus
    if (currentState == "running"):
        menus.menusTabs.select(menus.mainMenu.menusFrame)
        menus.mainMenu.runButton.grid_remove()
        menus.mainMenu.printCurrentLoadingDatas(mainData.dataCollection[mainData.generationLoop],
                                                            mainData.generationLoop,
                                                            applicationGUI.mainWindow,
                                                            mainData.generationsNb)
    else:
        applicationGUI.menus.mainMenu.printCurrentLoadingDatas(None, 0, None, 0)

def spawnCurrentLoopFood(mainData, mapRepresentation):
    foodList = []
    foodList.append(getFoodListFromMapRepresentation(mainData))
    return foodList

def spawnCurrentLoopGeneration(applicationGUI, mainData):
    populationList = spawnNewGeneration(applicationGUI, mainData)
    return populationList

def storeCurrentLoopData(populationList, foodList, mainData, mapRepresentation):
    populationList = runCurrentGenerationLife(populationList, mainData,
                                              mapRepresentation, foodList)
    mainData.allGenerationsPopulationList.append(populationList)
    mainData.allGenerationsFoodList.append(foodList)
    mainData.dataCollection.append(DataCollection(populationList, mainData))
    return populationList


def main():
    applicationGUI = initGUIApplication(winWidth, winHeight, runGenerationsLife)
    applicationGUI.mainWindow.mainloop()

if (__name__ == "__main__"):
    main()

