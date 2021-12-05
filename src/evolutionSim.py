from gui.guiWindow import initGUIApplication
from population.population import spawnNewGeneration
from population.population import runCurrentGenerationLife
from environment.food import spawnGenerationFood
from debug.print import *
from environment.mapRepresentation import *

populationNb = 5
winWidth = 1500
winHeight = 750
mapSizeX = 5
mapSizeY = 7
generationLifeSpan = 1
foodNb = populationNb
foodVariation = 0

# Initiate GUI components
applicationGUI = initGUIApplication(winWidth, winHeight, mapSizeX, mapSizeY)

mapRepresentation = createMapRepresentation(mapSizeX, mapSizeY)
# init first Generation
populationList = spawnNewGeneration(populationNb, mapSizeX, mapSizeY, None)
mapRepresentation = addPopulationListToMapRepresentation(populationList,
                                                         mapRepresentation)

foodList = spawnGenerationFood(foodNb, foodVariation, applicationGUI.mapSizeX,
                               applicationGUI.mapSizeY, mapRepresentation)
mapRepresentation = addFoodListToMapRepresentation(foodList, mapRepresentation)

populationList = runCurrentGenerationLife(populationList, generationLifeSpan,
                         mapSizeX, mapSizeY, mapRepresentation)

printPopulationListPositions(populationList)
printFoodListPositions(foodList)
printPopulationListCurrentGoal(populationList)

applicationGUI.printPopulationOnMap(populationList)
applicationGUI.printFoodOnMap(foodList)
applicationGUI.runApplicationGUI()
