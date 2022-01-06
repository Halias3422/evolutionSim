import sys
import tkinter as tk
from PIL import Image, ImageTk, ImageColor

class PrintRunResult:
    loopIndex = 0
    prevLoopIndex = -1
    currGeneration = 0
    mouseXClick = -1
    mouseYClick = -1
    prevMouseXClick = -1
    prevMouseYClick = -1

    def __init__(self, mainData, applicationGUI):
        self.applicationGUI = applicationGUI
        self.generationLifeSpan = mainData.generationLifeSpan
        self.generationsPopulationList = mainData.allGenerationsPopulationList
        self.generationsFoodList = mainData.allGenerationsFoodList
        self.generationsNb = mainData.generationsNb
        applicationGUI.menus.mainMenu.runButton.grid()
        applicationGUI.map.bind("<Button-1>", self.__mouseClick)
        applicationGUI.menus.enableRunInfoTab()
        applicationGUI.menus.menusTabs.select(applicationGUI.menus.runInfoMenu.runInfoFrame)
        applicationGUI.menus.runInfoMenu.progressBarsFrame.grid()
        applicationGUI.menus.runInfoMenu.setBarsRunValues(mainData)

        self.__launchDisplayLoop(applicationGUI, mainData)

    def __mouseClick(self, event):
        self.mouseXClick = event.x
        self.mouseYClick = event.y

    def __moveLoopIndex(self, value):
        self.loopIndex += value
        self.applicationGUI.menus.runInfoMenu.correctProgressValues(self.currGeneration,
                                                                   self.loopIndex)

    def setLoopIndexFromMenu(self, value):
        self.loopIndex = value


    def __keyPressedDuringReplay(self, event):
        if (event.keysym == "Left"):
            self.__moveLoopIndex(-1)
        elif (event.keysym == "Right"):
            self.__moveLoopIndex(1)
        # elif (event.keysym == "Return"):
        #     self.loopIndex = self.generationLifeSpan

    def __printPopulationOnMap(self, populationList, mapContent, applicationGUI):
        for individual in populationList:
            startX = individual.mapPosition[self.loopIndex][1] * applicationGUI.XCellSize
            startY = individual.mapPosition[self.loopIndex][0] * applicationGUI.YCellSize
            mapContent.append({
                "type": "individual",
                "name": individual.name,
                "startX": startX,
                "startY": startY,
                "endX": startX + applicationGUI.XCellSize,
                "endY": startY + applicationGUI.YCellSize,
                "posX": startX / applicationGUI.XCellSize,
                "posY": startY / applicationGUI.YCellSize,
                "hasReproduced": individual.hasReproduced,
                "hasReproducedLoop": individual.hasReproducedLoop,
                "hasEaten": individual.hasEaten,
                "hasEatenLoop": individual.hasEatenLoop,
                "genePool": individual.genePool,
                "currentGoal": individual.currentGoalHistory[self.loopIndex - 1],
                "currentGoalPos": individual.currGoalPosHistory[self.loopIndex - 1]
                })
            color = "black"
            if (individual.hasEaten is True
                and individual.hasEatenLoop <= self.loopIndex
                and individual.hasReproduced is True
                and individual.hasReproducedLoop <= self.loopIndex):
                color = "yellow"
            elif (individual.hasEaten is True
                  and individual.hasEatenLoop <= self.loopIndex):
                color = "red"
            elif (individual.hasReproduced is True
                  and individual.hasReproducedLoop <= self.loopIndex):
                color = "pink"
            applicationGUI.map.create_rectangle(startX,
                                      startY,
                                      startX + applicationGUI.XCellSize,
                                      startY + applicationGUI.YCellSize,
                                      fill=color)

    def __printObstaclesOnMap(self, mainData, mapContent, applicationGUI):
        for obstacle in mainData.obstacleList:
            startX = obstacle[1] * applicationGUI.XCellSize
            startY = obstacle[0] * applicationGUI.YCellSize
            mapContent.append({
                "type": "obstacle",
                "startX": startX,
                "startY": startY,
                "posX": startX / applicationGUI.XCellSize,
                "posY": startY / applicationGUI.YCellSize,
                "endX": startX + applicationGUI.XCellSize,
                "endY": startY + applicationGUI.YCellSize})
            applicationGUI.map.create_rectangle(startX,
                                      startY,
                                      startX + applicationGUI.XCellSize,
                                      startY + applicationGUI.YCellSize,
                                      fill="chocolate")

    def __printFoodOnMap(self, foodList, mapContent, applicationGUI):
        for food in foodList:
            startX = food[1] * applicationGUI.XCellSize
            startY = food[0] * applicationGUI.YCellSize
            mapContent.append({
                "type": "food",
                "startX": startX,
                "startY": startY,
                "posX": startX / applicationGUI.XCellSize,
                "posY": startY / applicationGUI.YCellSize,
                "endX": startX + applicationGUI.XCellSize,
                "endY": startY + applicationGUI.YCellSize})
            applicationGUI.map.create_rectangle(startX,
                                      startY,
                                      startX + applicationGUI.XCellSize,
                                      startY + applicationGUI.YCellSize,
                                      fill="green")

    def __createHoveringDangerZoneOnMap(self, applicationGUI, dangerZone, **options):
        if ("alpha" in options):
            alpha = int(options.pop("alpha") * 255)
            fill = options.pop("fill")
            if (fill == "grey"):
                fill = (128, 128, 128, 96)
            try:
                image = Image.new("RGBA", (int(dangerZone["endX"]) -
                                  int(dangerZone["startX"]),
                                  int(dangerZone["endY"]) -
                                  int(dangerZone["startY"])), fill)
                self.dangerImages.append(ImageTk.PhotoImage(image))
            except:
                return
            applicationGUI.map.create_image(dangerZone["startX"], dangerZone["startY"],
                    image=self.dangerImages[-1], anchor='nw')

    def __printDangerOnMap(self, mainData, applicationGUI):
        self.dangerImages = []
        for danger in mainData.dangerList:
            startX = danger[1] * applicationGUI.XCellSize
            startY = danger[0] * applicationGUI.YCellSize
            dangerZone = {
                    "startX": startX,
                    "startY": startY,
                    "endX": startX + applicationGUI.XCellSize,
                    "endY": startY + applicationGUI.YCellSize
                    }
            self.__createHoveringDangerZoneOnMap(applicationGUI, dangerZone,
                                                 fill="grey", alpha=.5)


    def __printSurvivingIndividuals(self, populationList, mapContent, applicationGUI):
        for individual in populationList:
            if (individual.hasEaten is True
                and individual.hasReproduced is True
                and individual.escapedDanger is True):
                startX = individual.currMapPosition[1] * applicationGUI.XCellSize
                startY = individual.currMapPosition[0] * applicationGUI.YCellSize
                applicationGUI.map.create_rectangle(startX,
                                          startY,
                                          startX + applicationGUI.XCellSize,
                                          startY + applicationGUI.YCellSize,
                                          fill="yellow")
                mapContent.append({
                    "type": "individual",
                    "name": individual.name,
                    "posX": startX / applicationGUI.XCellSize,
                    "posY": startY / applicationGUI.YCellSize,
                    "startX": startX,
                    "startY": startY,
                    "endX": startX + applicationGUI.XCellSize,
                    "endY": startY + applicationGUI.YCellSize,
                    "hasReproduced": individual.hasReproduced,
                    "hasReproducedLoop": individual.hasReproducedLoop,
                    "hasEaten": individual.hasEaten,
                    "hasEatenLoop": individual.hasEatenLoop,
                    "genePool": individual.genePool,
                    "currentGoal": "Give birth",
                    "currentGoalPos": "None"
                    })

    def __addContentForCurrentFrameToMap(self, applicationGUI, populationList,
                                         foodList, mapContent, mainData):
        applicationGUI.map.delete("all")
        applicationGUI.createMapGrid(applicationGUI.mapSizeX, applicationGUI.mapSizeY)
        if (self.loopIndex < self.generationLifeSpan):
            self.__printPopulationOnMap(populationList, mapContent, applicationGUI)
            self.__printFoodOnMap(foodList[self.loopIndex], mapContent, applicationGUI)
            self.__printObstaclesOnMap(mainData, mapContent, applicationGUI)
            self.__printDangerOnMap(mainData, applicationGUI)
        else:
            self.__printSurvivingIndividuals(populationList, mapContent, applicationGUI)
        applicationGUI.map.pack()
        applicationGUI.mainWindow.update()

    def __checkWhatIsUnderClickPosition(self, mapContent):
        for content in mapContent:
            if (content["startX"] <= self.mouseXClick and
                    content["endX"] >= self.mouseXClick
                and content["startY"] <= self.mouseYClick and
                content["endY"] >= self.mouseYClick):
                    return content
        return None

    def __checkLoopIndexNewValue(self, applicationGUI):
        if (self.loopIndex < 0 and self.currGeneration > 0):
            self.loopIndex = self.generationLifeSpan
            self.currGeneration -= 1
        elif (self.loopIndex < 0):
            self.loopIndex = 0
        elif (self.loopIndex > self.generationLifeSpan
              and self.currGeneration < self.generationsNb - 1):
            self.loopIndex = 0
            self.currGeneration += 1
        elif (self.loopIndex > self.generationLifeSpan):
            self.loopIndex = self.generationLifeSpan
        applicationGUI.menus.runInfoMenu.correctProgressValues(self.currGeneration,
                                                               self.loopIndex)

    def __checkCurrGenerationNewValue(self):
        if (self.currGeneration < 0):
            self.currGeneration = 0
        elif (self.currGeneration >= self.generationsNb):
            self.currGeneration = self.generationsNb - 1

    def __runInfoMenuBarsValuesUpdated(self, applicationGUI):
        if (self.prevLoopIndex != self.loopIndex):
            applicationGUI.menus.runInfoMenu.correctProgressValues(self.currGeneration,
                                                                   self.loopIndex)
            self.__checkLoopIndexNewValue(applicationGUI)
            return True
        else:
            menuLoopIndex = applicationGUI.menus.runInfoMenu.loopIndex
            menuCurrGeneration = applicationGUI.menus.runInfoMenu.currGeneration
            if (menuCurrGeneration - 1 != self.currGeneration):
                self.currGeneration = menuCurrGeneration - 1
                self.__checkCurrGenerationNewValue()
            elif (menuLoopIndex != self.loopIndex):
                self.loopIndex = menuLoopIndex
                self.__checkLoopIndexNewValue(applicationGUI)
            else:
                return False
            applicationGUI.menus.runInfoMenu.correctProgressValues(self.currGeneration,
                                                                   self.loopIndex)
            return True

    def __launchDisplayLoop(self, applicationGUI, mainData):
        applicationGUI.mainWindow.bind("<Key>", self.__keyPressedDuringReplay)
        while True:
            if (applicationGUI.exiting is True):
                break
            if (self.__runInfoMenuBarsValuesUpdated(applicationGUI) is True):
                self.prevLoopIndex = self.loopIndex
                applicationGUI.menus.runInfoMenu.updatePopulationInfoFrame(mainData,
                                                                self.loopIndex,
                                                                self.currGeneration)
                mapContent = []
                self.__addContentForCurrentFrameToMap(applicationGUI,
                            self.generationsPopulationList[self.currGeneration],
                            self.generationsFoodList[self.currGeneration],
                            mapContent,
                            mainData)
                print("\rGen (" + str(self.currGeneration)
                      + ") loop " + str(self.loopIndex), end='\r')
            if ('mapContent' in locals() and (self.prevMouseXClick != self.mouseXClick
                or self.prevMouseYClick != self.mouseYClick)):
                clickedOnObject = self.__checkWhatIsUnderClickPosition(mapContent)
                if (clickedOnObject and clickedOnObject["type"] == "individual"):
                    applicationGUI.menus.runInfoMenu.printCurrentlySelectedIndividualInfo(clickedOnObject, applicationGUI.menus.menusTabs, self.loopIndex)
                elif (clickedOnObject and clickedOnObject["type"] == "food"):
                    applicationGUI.menus.runInfoMenu.printCurrentlySelectedFoodInfo(\
                            clickedOnObject, applicationGUI.menus.menusTabs)
                self.prevMouseXClick = self.mouseXClick
                self.prevMouseYClick = self.mouseYClick
            applicationGUI.mainWindow.update()


