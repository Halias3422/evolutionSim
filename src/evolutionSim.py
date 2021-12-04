from gui.guiWindow import initGUIApplication
from population.population import spawnNewGeneration
from population.population import runCurrentGenerationLife

populationNb = 11
winWidth = 1500
winHeight = 750
mapSizeX = 10
mapSizeY = 5
generationLifeSpan = 100

# Initiate GUI components
applicationGUI = initGUIApplication(winWidth, winHeight, mapSizeX, mapSizeY)

# init first Generation
populationList = spawnNewGeneration(populationNb, applicationGUI.mapSizeX,
                                    applicationGUI.mapSizeY, None)

runCurrentGenerationLife(populationList, generationLifeSpan,
                         mapSizeX, mapSizeY)


# applicationGUI.printPopulationOnMap(populationList)
applicationGUI.runApplicationGUI()
