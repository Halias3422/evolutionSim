from gui.guiWindow import initGUIApplication
from population.population import spawnNewGeneration
from population.population import runCurrentGenerationLife
from environment.food import spawnGenerationFood
from debug.print import *
from environment.mapRepresentation import *
from dataCollection.dataCollection import DataCollection

populationNb = 1000
winWidth = 1500
winHeight = 750
mapSizeX = 100
mapSizeY = 100
generationLifeSpan = 100
foodNb = populationNb / 2
foodVariation = 0

dataCollection = []
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
                                          mapRepresentation, foodList)

dataCollection.append(DataCollection(populationList))
printDataCollectionForCurrentGeneration(dataCollection[0])

applicationGUI.printGenerationLifeSpanFrameByFrame(populationList, foodList,
                                    generationLifeSpan)
applicationGUI.runApplicationGUI()
