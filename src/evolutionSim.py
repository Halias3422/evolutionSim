from gui.guiWindow import initGUIApplication
from population.population import initFirstGeneration

populationNb = 10
winWidth = 1500
winHeight = 750
mapSizeX = 10
mapSizeY = 15

# Initiate GUI components
applicationGUI = initGUIApplication(winWidth, winHeight, mapSizeX, mapSizeY)

populationList = initFirstGeneration(populationNb, applicationGUI.mapSizeX,
                                     applicationGUI.mapSizeY)
for individual in populationList:
    print(individual.mapPosition)
applicationGUI.printPopulationOnMap(populationList)


applicationGUI.runApplicationGUI()
