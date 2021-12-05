from gui.guiWindow import initGUIApplication
from population.population import spawnNewGeneration
from population.population import runCurrentGenerationLife
from environment.food import spawnGenerationFood
from debug.print import *
from environment.mapRepresentation import *

populationNb = 5000
winWidth = 1500
winHeight = 750
mapSizeX = 200
mapSizeY = 200
generationLifeSpan = 100
foodNb = populationNb / 2
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
                                          mapRepresentation)

applicationGUI.printGenerationLifeSpanFrameByFrame(populationList, foodList,
                                    generationLifeSpan)
applicationGUI.runApplicationGUI()
