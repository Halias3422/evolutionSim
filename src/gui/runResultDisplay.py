import sys
import tkinter as tk
from PIL import Image, ImageTk, ImageColor, ImageDraw

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
        self.registeredLoopsMapContent = []
        self.registeredLoopsImages = []
        applicationGUI.menus.mainMenu.runButton.grid()
        applicationGUI.map.bind("<Button-1>", self.__mouseClick)
        applicationGUI.menus.enableRunInfoTab()
        applicationGUI.menus.menusTabs.select(applicationGUI.menus.runInfoMenu.runInfoFrame)
        applicationGUI.menus.runInfoMenu.progressBarsFrame.grid()
        applicationGUI.menus.runInfoMenu.setBarsRunValues(mainData)

        self.__registerLoopsDisplay(applicationGUI, mainData)
        self.__launchDisplayLoop(applicationGUI, mainData)

    def __registerLoopsDisplay(self, applicationGUI, mainData):
        self.__printDangerZonesOnMap(mainData, applicationGUI)
        self.registerGenerationNb = 0
        while (self.registerGenerationNb < self.generationsNb):
            self.registerLoopIndex = 0
            self.currGenerationImages = []
            self.registerLoopMapContent = []
            while (self.registerLoopIndex <= self.generationLifeSpan):
                mapContent = []
                self.__addContentForCurrentFrameToMap(applicationGUI,
                        self.generationsPopulationList[self.registerGenerationNb],
                        self.generationsFoodList[self.registerGenerationNb],
                        mapContent,
                        mainData)
                self.currGenerationImages.append(ImageTk.PhotoImage(image=self.loopImage))
                self.registerLoopMapContent.append(mapContent)
                self.registerLoopIndex += 1
            self.registeredLoopsMapContent.append(self.registerLoopMapContent)
            self.registeredLoopsImages.append(self.currGenerationImages)
            self.registerGenerationNb += 1

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
                self.__printCurrentLoopToMap(applicationGUI)
            if (self.prevMouseXClick != self.mouseXClick
                or self.prevMouseYClick != self.mouseYClick):
                clickedOnObject = self.__checkWhatIsUnderClickPosition(self.registeredLoopsMapContent[self.currGeneration][self.loopIndex])
                if (clickedOnObject and clickedOnObject["type"] == "individual"):
                    applicationGUI.menus.runInfoMenu.printCurrentlySelectedIndividualInfo(clickedOnObject, applicationGUI.menus.menusTabs, self.loopIndex)
                elif (clickedOnObject and clickedOnObject["type"] == "food"):
                    applicationGUI.menus.runInfoMenu.printCurrentlySelectedFoodInfo(\
                            clickedOnObject, applicationGUI.menus.menusTabs)
                self.prevMouseXClick = self.mouseXClick
                self.prevMouseYClick = self.mouseYClick
            applicationGUI.mainWindow.update()

    def __createMapGrid(self, applicationGUI):
        currPosY = applicationGUI.frameHeight
        while (currPosY >= 0):
            self.loopDraw.line([0, currPosY, applicationGUI.frameLength, currPosY],
                    fill="black")
            currPosY -= applicationGUI.YCellSize
        currPosX = applicationGUI.frameLength
        while (currPosX >= 0):
            self.loopDraw.line([currPosX, 0, currPosX, applicationGUI.frameHeight],
                    fill="black")
            currPosX -= applicationGUI.XCellSize

    def __printCurrentLoopToMap(self, applicationGUI):
        applicationGUI.map.delete("all")
        applicationGUI.map.create_image(0, 0,
                image=self.registeredLoopsImages[self.currGeneration][self.loopIndex],
                anchor='nw')
        applicationGUI.map.create_image(0, 0,
                image=self.dangerMapImage,
                anchor='nw')

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

    def __printPopulationOnMap(self, populationList, mapContent, applicationGUI):
        for individual in populationList:
            startX = individual.mapPosition[self.registerLoopIndex][1] * applicationGUI.XCellSize
            startY = individual.mapPosition[self.registerLoopIndex][0] * applicationGUI.YCellSize
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
                "currentGoal": individual.currentGoalHistory[self.registerLoopIndex - 1],
                "currentGoalPos": individual.currGoalPosHistory[self.registerLoopIndex - 1]
                })
            color = "black"
            if (individual.hasEaten is True
                and individual.hasEatenLoop <= self.registerLoopIndex
                and individual.hasReproduced is True
                and individual.hasReproducedLoop <= self.registerLoopIndex):
                color = "yellow"
            elif (individual.hasEaten is True
                  and individual.hasEatenLoop <= self.registerLoopIndex):
                color = "red"
            elif (individual.hasReproduced is True
                  and individual.hasReproducedLoop <= self.registerLoopIndex):
                color = "pink"
            self.loopDraw.rectangle([startX, startY, startX + applicationGUI.XCellSize,
                                     startY + applicationGUI.YCellSize], fill=color)

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
            self.loopDraw.rectangle([startX, startY, startX + applicationGUI.XCellSize,
                                     startY + applicationGUI.YCellSize], fill=chocolate)

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
            self.loopDraw.rectangle([startX, startY, startX + applicationGUI.XCellSize,
                                     startY + applicationGUI.YCellSize], fill="green")

    def __printSurvivingIndividuals(self, populationList, mapContent, applicationGUI,
                                    mainData):
        for individual in populationList:
            if ((individual.hasEaten is True or mainData.foodToggle is True)
                and (individual.hasReproduced is True
                    or mainData.reproductionToggle is True)
                and individual.escapedDanger is True):
                startX = individual.currMapPosition[1] * applicationGUI.XCellSize
                startY = individual.currMapPosition[0] * applicationGUI.YCellSize
                self.loopDraw.rectangle([startX, startY,
                                       startX + applicationGUI.XCellSize,
                                       startY + applicationGUI.YCellSize],
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
        self.loopImage = Image.new("RGB", (applicationGUI.map.winfo_reqwidth(),
                             applicationGUI.map.winfo_reqheight()), "white")
        self.loopDraw = ImageDraw.Draw(self.loopImage)
        if (self.registerLoopIndex < self.generationLifeSpan):
            self.__printPopulationOnMap(populationList, mapContent, applicationGUI)
            self.__printFoodOnMap(foodList[self.registerLoopIndex], mapContent, applicationGUI)
            self.__printObstaclesOnMap(mainData, mapContent, applicationGUI)
        else:
            self.__printSurvivingIndividuals(populationList, mapContent, applicationGUI,
                                             mainData)
        self.__createMapGrid(applicationGUI)
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

    def __createHoveringDangerZoneOnMap(self, applicationGUI, dangerZone, **options):
        if ("alpha" in options):
            alpha = int(options.pop("alpha") * 255)
            fill = options.pop("fill")
            if (fill == "grey"):
                fill = (128, 128, 128, 96)
            self.dangerMapDraw.rectangle([int(dangerZone["startX"]),
                                          int(dangerZone["startY"]),
                                          int(dangerZone["endX"]),
                                          int(dangerZone["endY"])],
                                          fill)

    def __printDangerZonesOnMap(self, mainData, applicationGUI):
        self.dangerMapImage = Image.new("RGBA", (applicationGUI.map.winfo_reqwidth(),
                                        applicationGUI.map.winfo_reqheight()),
                                        (255, 255, 255, 0))
        self.dangerMapDraw = ImageDraw.Draw(self.dangerMapImage)
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
        self.dangerMapImage = ImageTk.PhotoImage(image=self.dangerMapImage)
