import tkinter as tk
from tkinter import ttk
import threading
import keyboard
from .mainMenu import MainMenu
from .menus import Menus

mouseXClick = -1
mouseYClick = -1

LABELFONT = ("Arial", 16)
DEFAULTPOPSIZE = 10
DEFAULTFOODNB = 0
DEFAULTFOODVARIATION = 0
DEFAULTMAPSIZE=5
DEFAULTGENLIFE=100
DEFAULTGENNB=1
DEFAULTMUTATION=100

class ApplicationGUI:

    def __init__(self, winWidth, winHeight):
        self.winWidth = winWidth
        self.winHeight = winHeight

    def createApplicationWindow(self):
        self.mainWindow = tk.Tk()
        self.mainWindow.geometry(str(self.winWidth) + "x" +
                                 str(self.winHeight))

    def createMainFrames(self, runGenerationsLife):
        self.frameLength = self.winWidth / 2
        self.frameHeight = self.winHeight
        self.mapFrame = tk.Frame(self.mainWindow, width=self.frameLength,
                                 height=self.frameHeight, bg="blue")
        self.mapFrame.pack(side=tk.LEFT)
        self.menus = Menus(self.mainWindow, self.frameLength, self.frameHeight,
                           runGenerationsLife, self)
        self.mainWindow.update_idletasks()


    def createMap(self, mapSizeX, mapSizeY):
        # self.mapSizeX = mapSizeX
        # self.mapSizeY= mapSizeY
        self.map = tk.Canvas(self.mapFrame, bg="white",
                             width=self.mapFrame.winfo_width(),
                             height=self.mapFrame.winfo_height())
        # self.XCellSize = self.frameLength / self.mapSizeX
        # self.YCellSize = self.frameHeight / self.mapSizeY
        self.map.pack()

    def defineMapSize(self, mapSizeX, mapSizeY):
        self.mapSizeX = mapSizeX
        self.mapSizeY = mapSizeY
        self.XCellSize = self.frameLength / self.mapSizeX
        self.YCellSize = self.frameHeight / self.mapSizeY

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
                "genePool": individual.genePool,
                "currentGoal": individual.currentGoalHistory[loopIndex - 1],
                "currentGoalPos": individual.currGoalPosHistory[loopIndex - 1]
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
                    "genePool": individual.genePool,
                    "currentGoal": "Give birth",
                    "currentGoalPos": "None"
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
        infoMenu = self.menus.runInfoFrame.runInfoMenu
        lblGenePool = tk.Label(infoMenu,
                               font=LABELFONT,
                               text="Gene Pool : ")
        lblMovement = tk.Label(infoMenu,
                               font=LABELFONT,
                               text="Movement: " + str(genePool.movement))
        lblDangerRadar = tk.Label(infoMenu,
                                  font=LABELFONT,
                                  text="Danger Radar: " + str(genePool.dangerRadar))
        lblFoodRadar = tk.Label(infoMenu,
                                font=LABELFONT,
                                text="Food Radar: " + str(genePool.foodRadar))
        lblReproductionRadar = tk.Label(infoMenu,
                                        font=LABELFONT,
                                        text="Reproduction Radar: "
                                        + str(genePool.reproductionRadar))
        lblFertility = tk.Label(infoMenu,
                                  font=LABELFONT,
                                  text="Fertility: " + str(genePool.fertility))
        lblPreference = tk.Label(infoMenu,
                                  font=LABELFONT,
                                  text="Preference: " + str(genePool.preference))
        lblFear = tk.Label(infoMenu,
                                  font=LABELFONT,
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
        # for widget in self.selectedItemTab.winfo_children():
        infoMenu = self.menus.runInfoFrame.runInfoMenu
        for widget in infoMenu.winfo_children():
            widget.destroy()
        if (clickedOnObject["type"] == "individual"):
            lblName = tk.Label(infoMenu,
                               font=LABELFONT,
                               text="Object = Individual " + clickedOnObject["name"])
            if (loopIndex >= clickedOnObject["hasReproducedLoop"]):
                lblHasReproduced = tk.Label(infoMenu,
                                            font=LABELFONT,
                    text="Has reproduced : " + str(clickedOnObject["hasReproduced"]))
            else:
                lblHasReproduced = tk.Label(infoMenu,
                                            font=LABELFONT,
                        text="Has reproduced : False")
            if (loopIndex >= clickedOnObject["hasEatenLoop"]):
                lblHasEaten = tk.Label(infoMenu,
                                       font=LABELFONT,
                    text="Has eaten : " + str(clickedOnObject["hasEaten"]))
            else:
                lblHasEaten = tk.Label(infoMenu,
                                       font=LABELFONT,
                        text="Has eaten : False")
            lblCurrentGoal = tk.Label(infoMenu,
                                      font=LABELFONT,
                                      text="Current Goal : "
                                      + clickedOnObject["currentGoal"])
            lblCurrentGoalPos = tk.Label(infoMenu,
                                         font=LABELFONT,
                                         text="Current Goal Pos : "
                                         + str(clickedOnObject["currentGoalPos"]))
        else:
            lblName = tk.Label(infoMenu,
                               font=LABELFONT,
                               text="Object = Food")
        lblCoord = tk.Label(infoMenu,
                            font=LABELFONT,
                text="Position : [" + str(clickedOnObject["startY"] / self.XCellSize)
                            + ", " + str(clickedOnObject["startX"] / self.YCellSize)
                            + "]")
        lblCurrentLoop = tk.Label(infoMenu,
                                  font=LABELFONT,
                                  text="Current Loop : "
                                  + str(loopIndex))
        lblName.pack()
        lblCoord.pack()
        if (clickedOnObject["type"] == "individual"):
            lblHasReproduced.pack()
            lblHasEaten.pack()
            lblCurrentGoal.pack()
            lblCurrentGoalPos.pack()
            self.printSelectedIndividualGenePool(clickedOnObject["genePool"])
        lblCurrentLoop.pack()
        infoMenu.pack_propagate(0)
        self.menus.menusTabs.select(infoMenu)

    def mouseClick(self, event):
        global mouseXClick
        global mouseYClick
        mouseXClick = event.x
        mouseYClick = event.y

    def keyPressedDuringReplay(self, event):
        if (event.keysym == "h" and self.loopIndex > 0):
            self.loopIndex -= 1
        elif (event.keysym == "l"):
            self.loopIndex += 1
        elif (event.keysym == "Escape"):
            self.loopIndex = -1
        elif (event.keysym == "Return"):
            self.loopIndex = self.generationLifeSpan

    def printGenerationsLifeSpanFrameByFrame(self, allGenerationsPopulationList,
                                             allGenerationsFoodList,
                                            generationLifeSpan,
                                            generationsNb):
        self.loopIndex = 0
        self.currGeneration = 0
        self.generationLifeSpan = generationLifeSpan
        print("press l to go forward, h to go backward or enter to quit")
        self.map.bind("<Button-1>", self.mouseClick)
        prevMouseXClick = mouseXClick
        prevMouseYClick = mouseYClick

        prevLoopIndex = self.loopIndex - 1
        self.mainWindow.bind("<Key>", self.keyPressedDuringReplay)
        while True:
            if (prevLoopIndex != self.loopIndex):
                prevLoopIndex = self.loopIndex
                if (self.loopIndex == -1):
                    exit()
                elif (self.loopIndex < 0 and self.currGeneration > 0):
                    self.loopIndex = generationLifeSpan
                    self.currGeneration -= 1
                elif (self.loopIndex < 0):
                    self.loopIndex = 0
                elif (self.loopIndex > generationLifeSpan
                      and self.currGeneration < generationsNb - 1):
                    self.loopIndex = 0
                    self.currGeneration += 1
                elif (self.loopIndex > generationLifeSpan):
                    self.loopIndex = generationLifeSpan
                mapContent = []
                self.addContentForCurrentFrameToMap(allGenerationsPopulationList[self.currGeneration],
                                                    allGenerationsFoodList[self.currGeneration],
                                                    self.loopIndex,
                                                    generationLifeSpan,
                                                    mapContent)
                print("\rGen (" + str(self.currGeneration)
                      + ") loop " + str(self.loopIndex), end='\r')
            if ('mapContent' in locals() and (prevMouseXClick != mouseXClick or
                prevMouseYClick != mouseYClick)):
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
    applicationGUI.createMainFrames(runGenerationsLife)
    applicationGUI.createMap(0, 0)
    return applicationGUI

def createGUImap(applicationGUI, mapSizeX, mapSizeY):
    applicationGUI.defineMapSize(mapSizeX, mapSizeY)
