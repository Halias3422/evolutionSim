from gui.guiWindow import initGUIApplication
from population.population import spawnNewGeneration
from population.population import runCurrentGenerationLife
from population.population import removeAllUnsuccessfullIndividuals
from environment.food import spawnGenerationFood
from debug.print import *
from environment.mapRepresentation import *
from dataCollection.dataCollection import DataCollection

populationNb = 400
winWidth = 1500
winHeight = 750
mapSizeX = 100
mapSizeY = 100
generationLifeSpan = 200
foodNb = populationNb
foodVariation = 0

dataCollection = []
# Initiate GUI components
applicationGUI = initGUIApplication(winWidth, winHeight, mapSizeX, mapSizeY)

mapRepresentation = createMapRepresentation(mapSizeX, mapSizeY)
# init first Generation
populationList = spawnNewGeneration(populationNb, mapSizeX, mapSizeY,
                                    generationLifeSpan, None)
mapRepresentation = addPopulationListToMapRepresentation(populationList,
                                                         mapRepresentation)
printMapRepresentation(mapRepresentation)

foodList = []
foodList.append(spawnGenerationFood(foodNb, foodVariation, applicationGUI.mapSizeX,
                               applicationGUI.mapSizeY, mapRepresentation))
mapRepresentation = addFoodListToMapRepresentation(foodList[0], mapRepresentation)

populationList = runCurrentGenerationLife(populationList, generationLifeSpan,
                                          mapRepresentation, foodList)

dataCollection.append(DataCollection(populationList))
printDataCollectionForCurrentGeneration(dataCollection[0])

applicationGUI.printGenerationLifeSpanFrameByFrame(populationList, foodList,
                                    generationLifeSpan)
populationList = removeAllUnsuccessfullIndividuals(populationList)
applicationGUI.runApplicationGUI()
