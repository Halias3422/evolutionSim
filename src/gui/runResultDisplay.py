import sys

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
        applicationGUI.map.bind("<Button-1>", self.__mouseClick)
        applicationGUI.menus.enableRunInfoTab()
        applicationGUI.menus.menusTabs.select(applicationGUI.menus.runInfoMenu.runInfoFrame)
        applicationGUI.menus.runInfoMenu.progressBarsFrame.grid()
        applicationGUI.menus.runInfoMenu.setBarsRunValues(mainData)

        self.__launchDisplayLoop(applicationGUI)

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

    def __printFoodOnMap(self, foodList, mapContent, applicationGUI):
        for food in foodList:
            startX = food[1] * applicationGUI.XCellSize
            startY = food[0] * applicationGUI.YCellSize
            mapContent.append({
                "type": "food",
                "startX": startX,
                "startY": startY,
                "endX": startX + applicationGUI.XCellSize,
                "endY": startY + applicationGUI.YCellSize})
            applicationGUI.map.create_rectangle(startX,
                                      startY,
                                      startX + applicationGUI.XCellSize,
                                      startY + applicationGUI.YCellSize,
                                      fill="green")

    def __printSurvivingIndividuals(self, populationList, mapContent, applicationGUI):
        for individual in populationList:
            if (individual.hasEaten is True
                and individual.hasReproduced is True):
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
                                         foodList, mapContent):
        applicationGUI.map.delete("all")
        # self.__createMapGrid()
        if (self.loopIndex < self.generationLifeSpan):
            self.__printPopulationOnMap(populationList, mapContent, applicationGUI)
            self.__printFoodOnMap(foodList[self.loopIndex], mapContent, applicationGUI)
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
            print("JE SUIS BIEN LA")
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

    def __launchDisplayLoop(self, applicationGUI):
        applicationGUI.mainWindow.bind("<Key>", self.__keyPressedDuringReplay)
        while True:
            if (self.__runInfoMenuBarsValuesUpdated(applicationGUI) is True):
                self.prevLoopIndex = self.loopIndex
                mapContent = []
                print("self = " + str(self.loopIndex))
                self.__addContentForCurrentFrameToMap(applicationGUI,
                            self.generationsPopulationList[self.currGeneration],
                            self.generationsFoodList[self.currGeneration],
                            mapContent)
                print("\rGen (" + str(self.currGeneration)
                      + ") loop " + str(self.loopIndex), end='\r')
            if ('mapContent' in locals() and (self.prevMouseXClick != self.mouseXClick
                or self.prevMouseYClick != self.mouseYClick)):
                clickedOnObject = self.__checkWhatIsUnderClickPosition(mapContent)
                if (clickedOnObject):
                    applicationGUI.menus.runInfoMenu.printCurrentlySelectedIndividualInfo(clickedOnObject, applicationGUI.menus.menusTabs)
                self.prevMouseXClick = self.mouseXClick
                self.prevMouseYClick = self.mouseYClick
            applicationGUI.mainWindow.update()


