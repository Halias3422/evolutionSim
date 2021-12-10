import tkinter as tk
from tkinter import ttk
import threading
import keyboard

mouseXClick = -1
mouseYClick = -1

class ApplicationGUI:

    def __init__(self, winWidth, winHeight):
        self.winWidth = winWidth
        self.winHeight = winHeight

    def createApplicationWindow(self):
        self.mainWindow = tk.Tk()
        self.mainWindow.geometry(str(self.winWidth) + "x" +
                                 str(self.winHeight))

    def createMainFrames(self):
        self.frameLength = self.winWidth / 2
        self.frameHeight = self.winHeight
        self.mapFrame = tk.Frame(self.mainWindow, width=self.frameLength,
                                 height=self.frameHeight, bg="blue")
        self.mapFrame.pack(side=tk.LEFT)
        self.optionsFrame = tk.Frame(self.mainWindow, width=self.frameLength,
                                     height=self.frameHeight, bg="green")
        self.optionsFrame.pack(side=tk.RIGHT)
        self.mainWindow.update_idletasks()

    def createOptionsTab(self):
        self.optionsNotebook = ttk.Notebook(self.optionsFrame)
        self.optionsNotebook.pack()
        self.optionsTab = tk.Frame(self.optionsNotebook,
                                   width=self.optionsFrame.winfo_width(),
                                   height=self.optionsFrame.winfo_height())
        self.selectedItemTab = tk.Frame(self.optionsNotebook,
                                        width=self.optionsFrame.winfo_width(),
                                        height=self.optionsFrame.winfo_height())
        self.optionsTab.pack()
        self.selectedItemTab.pack()
        self.optionsNotebook.add(self.optionsTab, text="Run Options")
        self.optionsNotebook.add(self.selectedItemTab, text="Selected Item Infos")

    def fillRunOptionsTab(self, runGenerationsLife):
        lblPopulationSize = tk.Label(self.optionsTab,
                                     font=("Arial", 16),
                                     text="Population Size: ")
        lblPopulationSize.pack()
        self.txtPopulationSize = tk.Entry(self.optionsTab, font=("Arial", 16))
        self.txtPopulationSize.insert(0, "100")
        self.txtPopulationSize.pack()

        lblFoodNb = tk.Label(self.optionsTab,
                             font=("Arial", 16),
                             text="Food Units Available : ")
        lblFoodNb.pack()
        self.txtFoodNb = tk.Entry(self.optionsTab, font=("Arial", 16))
        self.txtFoodNb.insert(0, self.txtPopulationSize.get())
        self.txtFoodNb.pack()

        lblFoodVariation = tk.Label(self.optionsTab,
                                    font=("Arial", 16),
                                    text="Food Variation (%) : ")
        lblFoodVariation.pack()
        self.txtFoodVariation = tk.Entry(self.optionsTab, font=("Arial", 16))
        self.txtFoodVariation.insert(0, "0")
        self.txtFoodVariation.pack()

        lblMapSize = tk.Label(self.optionsTab, font=("Arial", 16),
                              text="Map Size (X and Y): ")
        lblMapSize.pack()
        self.txtMapSize = tk.Entry(self.optionsTab, font=("Arial", 16))
        self.txtMapSize.insert(0, "50")
        self.txtMapSize.pack()

        lblGenerationLifeSpan = tk.Label(self.optionsTab, font=("Arial", 16),
                                         text="Generation Life Span : ")
        lblGenerationLifeSpan.pack()
        self.txtGenerationLifeSpan = tk.Entry(self.optionsTab, font=("Arial", 16))
        self.txtGenerationLifeSpan.insert(0, "100")
        self.txtGenerationLifeSpan.pack()

        lblGenerationNb = tk.Label(self.optionsTab, font=("Arial", 16),
                                   text="Generations Number : ")
        lblGenerationNb.pack()
        self.txtGenerationNb = tk.Entry(self.optionsTab, font=("Arial", 16))
        self.txtGenerationNb.insert(0, "50")
        self.txtGenerationNb.pack()

        runButton = tk.Button(self.optionsTab, text=" Run ", font=("Arial", 16),
                              command=runGenerationsLife)
        runButton.bind("<Return>", runGenerationsLife)
        runButton.pack()
        runButton.focus_set()



    def createMap(self, mapSizeX, mapSizeY):
        self.mapSizeX = mapSizeX
        self.mapSizeY= mapSizeY
        self.map = tk.Canvas(self.mapFrame, bg="white",
                             width=self.mapFrame.winfo_width(),
                             height=self.mapFrame.winfo_height())
        self.XCellSize = self.frameLength / self.mapSizeX
        self.YCellSize = self.frameHeight / self.mapSizeY
        self.map.pack()

    def __createMapGrid(self):
        currPosY = self.frameHeight
        while (currPosY >= 0):
            self.map.create_line(0,
                                 currPosY,
                                 self.frameLength,
                                 currPosY,
                                 fill="black")
            currPosY -= self.YCellSize

        currPosX = self.frameLength
        while (currPosX >= 0):
            self.map.create_line(currPosX,
                                 0,
                                 currPosX,
                                 self.frameHeight,
                                 fill="black")
            currPosX -= self.XCellSize

    def runApplicationGUI(self):
        self.mainWindow.mainloop()

    def printPopulationOnMap(self, populationList, loopIndex, mapContent):
        for individual in populationList:
            startX = individual.mapPosition[loopIndex][1] * self.XCellSize
            startY = individual.mapPosition[loopIndex][0] * self.YCellSize
            mapContent.append({
                "type": "individual",
                "name": individual.name,
                "startX": startX,
                "startY": startY,
                "endX": startX + self.XCellSize,
                "endY": startY + self.YCellSize,
                "hasReproduced": individual.hasReproduced,
                "hasReproducedLoop": individual.hasReproducedLoop,
                "hasEaten": individual.hasEaten,
                "hasEatenLoop": individual.hasEatenLoop,
                "genePool": individual.genePool
                })
            color = "black"
            if (individual.hasEaten is True
                and individual.hasEatenLoop <= loopIndex
                and individual.hasReproduced is True
                and individual.hasReproducedLoop <= loopIndex):
                color = "yellow"
            elif (individual.hasEaten is True
                  and individual.hasEatenLoop <= loopIndex):
                color = "red"
            elif (individual.hasReproduced is True
                  and individual.hasReproducedLoop <= loopIndex):
                color = "pink"
            self.map.create_rectangle(startX,
                                      startY,
                                      startX + self.XCellSize,
                                      startY + self.YCellSize,
                                      fill=color)

    def printFoodOnMap(self, foodList, mapContent):
        for food in foodList:
            startX = food[1] * self.XCellSize
            startY = food[0] * self.YCellSize
            mapContent.append({
                "type": "food",
                "startX": startX,
                "startY": startY,
                "endX": startX + self.XCellSize,
                "endY": startY + self.YCellSize})
            self.map.create_rectangle(startX,
                                      startY,
                                      startX + self.XCellSize,
                                      startY + self.YCellSize,
                                      fill="green")

    def printSurvivingIndividuals(self, populationList, mapContent):
        for individual in populationList:
            if (individual.hasEaten is True
                and individual.hasReproduced is True):
                startX = individual.currMapPosition[1] * self.XCellSize
                startY = individual.currMapPosition[0] * self.YCellSize
                self.map.create_rectangle(startX,
                                          startY,
                                          startX + self.XCellSize,
                                          startY + self.YCellSize,
                                          fill="yellow")
                mapContent.append({
                    "type": "individual",
                    "name": individual.name,
                    "startX": startX,
                    "startY": startY,
                    "endX": startX + self.XCellSize,
                    "endY": startY + self.YCellSize,
                    "hasReproduced": individual.hasReproduced,
                    "hasReproducedLoop": individual.hasReproducedLoop,
                    "hasEaten": individual.hasEaten,
                    "hasEatenLoop": individual.hasEatenLoop,
                    "genePool": individual.genePool
                    })


    def addContentForCurrentFrameToMap(self, populationList, foodList,
                                       loopIndex, generationLifeSpan, mapContent):
        self.map.delete("all")
        # self.__createMapGrid()
        if (loopIndex < generationLifeSpan):
            self.printPopulationOnMap(populationList, loopIndex, mapContent)
            self.printFoodOnMap(foodList[loopIndex], mapContent)
        else:
            self.printSurvivingIndividuals(populationList, mapContent)
        self.map.pack()
        self.mainWindow.update()


    def checkWhatIsUnderClickPosition(self, mapContent,
                                      mouseXClick, mouseYClick):
        for content in mapContent:
            if (content["startX"] <= mouseXClick and content["endX"] >= mouseXClick
                and content["startY"] <= mouseYClick and content["endY"] >= mouseYClick):
                    return content
        return None

    def printSelectedIndividualGenePool(self, genePool):
        lblGenePool = tk.Label(self.selectedItemTab,
                               font=("Arial", 16),
                               text="Gene Pool : ")
        lblMovement = tk.Label(self.selectedItemTab,
                               font=("Arial", 16),
                               text="Movement: " + str(genePool.movement))
        lblDangerRadar = tk.Label(self.selectedItemTab,
                                  font=("Arial", 16),
                                  text="Danger Radar: " + str(genePool.dangerRadar))
        lblFoodRadar = tk.Label(self.selectedItemTab,
                                font=("Arial", 16),
                                text="Food Radar: " + str(genePool.foodRadar))
        lblReproductionRadar = tk.Label(self.selectedItemTab,
                                        font=("Arial", 16),
                                        text="Reproduction Radar: "
                                        + str(genePool.reproductionRadar))
        lblFertility = tk.Label(self.selectedItemTab,
                                  font=("Arial", 16),
                                  text="Fertility: " + str(genePool.fertility))
        lblPreference = tk.Label(self.selectedItemTab,
                                  font=("Arial", 16),
                                  text="Preference: " + str(genePool.preference))
        lblFear = tk.Label(self.selectedItemTab,
                                  font=("Arial", 16),
                                  text="Fear: " + str(genePool.fear))

        lblGenePool.pack(pady=(10, 0))
        lblMovement.pack()
        lblDangerRadar.pack()
        lblFoodRadar.pack()
        lblReproductionRadar.pack()
        lblFertility.pack()
        lblPreference.pack()
        lblFear.pack()


    def updateSelectedObjectDescriptionFrameContent(self, clickedOnObject, loopIndex):
        for widget in self.selectedItemTab.winfo_children():
            widget.destroy()
        if (clickedOnObject["type"] == "individual"):
            lblName = tk.Label(self.selectedItemTab,
                               font=("Arial", 16),
                               text="Object = Individual " + clickedOnObject["name"])
            if (loopIndex >= clickedOnObject["hasReproducedLoop"]):
                lblHasReproduced = tk.Label(self.selectedItemTab,
                                            font=("Arial", 16),
                    text="Has reproduced : " + str(clickedOnObject["hasReproduced"]))
            else:
                lblHasReproduced = tk.Label(self.selectedItemTab,
                                            font=("Arial", 16),
                        text="Has reproduced : False")
            if (loopIndex >= clickedOnObject["hasEatenLoop"]):
                lblHasEaten = tk.Label(self.selectedItemTab,
                                       font=("Arial", 16),
                    text="Has eaten : " + str(clickedOnObject["hasEaten"]))
            else:
                lblHasEaten = tk.Label(self.selectedItemTab,
                                       font=("Arial", 16),
                        text="Has eaten : False")
        else:
            lblName = tk.Label(self.selectedItemTab,
                               font=("Arial", 16),
                               text="Object = Food")
        lblCoord = tk.Label(self.selectedItemTab,
                            font=("Arial", 16),
                text="Position : [" + str(clickedOnObject["startX"] / self.XCellSize)
                            + ", " + str(clickedOnObject["startY"] / self.YCellSize)
                            + "]")
        lblName.pack()
        lblCoord.pack()
        if (clickedOnObject["type"] == "individual"):
            lblHasReproduced.pack()
            lblHasEaten.pack()
            self.printSelectedIndividualGenePool(clickedOnObject["genePool"])
        self.selectedItemTab.pack_propagate(0)
        self.optionsNotebook.select(self.selectedItemTab)

    def mouseClick(self, event):
        global mouseXClick
        global mouseYClick
        mouseXClick = event.x
        mouseYClick = event.y

    def keyPressedDuringReplay(self, event):
        if (event.keysym == "h"):
            self.loopIndex -= 1
        elif (event.keysym == "l"):
            self.loopIndex += 1
        elif (event.keysym == "Escape"):
            self.loopIndex = "exit"
        elif (event.keysym == "Return"):
            self.loopIndex = "end"

    def printGenerationLifeSpanFrameByFrame(self, populationList, foodList,
                                            generationLifeSpan):
        self.loopIndex = 0
        print("press l to go forward, h to go backward or enter to quit")
        self.map.bind("<Button-1>", self.mouseClick)
        prevMouseXClick = mouseXClick
        prevMouseYClick = mouseYClick

        prevLoopIndex = self.loopIndex
        self.mainWindow.bind("<Key>", self.keyPressedDuringReplay)
        while True:
            if (prevLoopIndex != self.loopIndex):
                prevLoopIndex = self.loopIndex
                if (self.loopIndex == "exit"):
                    exit()
                elif (self.loopIndex == "end"):
                    self.loopIndex = generationLifeSpan
                elif (self.loopIndex < 0):
                    self.loopIndex = 0
                elif (self.loopIndex > generationLifeSpan):
                    self.loopIndex = generationLifeSpan
                mapContent = []
                self.addContentForCurrentFrameToMap(populationList, foodList,
                                                    self.loopIndex, generationLifeSpan,
                                                    mapContent)
                print("loop " + str(self.loopIndex))
            if (prevMouseXClick != mouseXClick or
                prevMouseYClick != mouseYClick):
                clickedOnObject = self.checkWhatIsUnderClickPosition(mapContent,
                                                                     mouseXClick,
                                                                     mouseYClick)
                if (clickedOnObject):
                    self.updateSelectedObjectDescriptionFrameContent(clickedOnObject,
                                                                     self.loopIndex)
                prevMouseXClick = mouseXClick
                prevMouseYClick = mouseYClick
            self.mainWindow.update()


def initGUIApplication(winWidth, winHeight, runGenerationsLife):
    applicationGUI = ApplicationGUI(winWidth, winHeight)
    applicationGUI.createApplicationWindow()
    applicationGUI.createMainFrames()
    applicationGUI.createOptionsTab()
    applicationGUI.fillRunOptionsTab(runGenerationsLife)
    return applicationGUI

def createGUImap(applicationGUI, mapSizeX, mapSizeY):
    applicationGUI.createMap(mapSizeX, mapSizeY)
