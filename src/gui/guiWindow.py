import tkinter as tk
import threading
import keyboard
from debug.print import *

mouseXClick = -1
mouseYClick = -1

class ApplicationGUI:

    def __init__(self, winWidth, winHeight, mapSizeX, mapSizeY):
        self.winWidth = winWidth
        self.winHeight = winHeight
        self.mapSizeX = mapSizeX
        self.mapSizeY = mapSizeY

    def createApplicationWindow(self):
        self.mainWindow = tk.Tk()
        self.mainWindow.geometry(str(self.winWidth) + "x" +
                                 str(self.winHeight))

    def createMapFrame(self):
        self.frameLength = self.winWidth / 2
        self.frameHeight = self.winHeight
        self.mapFrame = tk.Frame(self.mainWindow, width=self.frameLength,
                                 height=self.frameHeight, bg="blue")
        self.mapFrame.pack(side=tk.LEFT)
        self.mainWindow.update_idletasks()

    def createMap(self):
        # self.map = tk.Canvas(self.mapFrame, bg="white",
        #                      width=self.frameLength,
        #                      height=self.frameHeight)
        self.map = tk.Canvas(self.mapFrame, bg="white",
                             width=self.mapFrame.winfo_width(),
                             height=self.mapFrame.winfo_height())
        self.XCellSize = self.frameLength / self.mapSizeX
        self.YCellSize = self.frameHeight / self.mapSizeY
        # self.__createMapGrid()
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
                "hasEaten": individual.hasEaten})
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

    def printSurvivingIndividuals(self, populationList):
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



    def addContentForCurrentFrameToMap(self, populationList, foodList,
                                       loopIndex, generationLifeSpan, mapContent):
        self.map.delete("all")
        # self.__createMapGrid()
        if (loopIndex < generationLifeSpan):
            self.printPopulationOnMap(populationList, loopIndex, mapContent)
            self.printFoodOnMap(foodList[loopIndex], mapContent)
        else:
            self.printSurvivingIndividuals(populationList)
        self.map.pack()
        self.mainWindow.update()


    def checkWhatIsUnderClickPosition(self, mapContent,
                                      mouseXClick, mouseYClick):
        for content in mapContent:
            if (content["startX"] <= mouseXClick and content["endX"] >= mouseXClick
                and content["startY"] <= mouseYClick and content["endY"] >= mouseYClick):
                    return content
        return None

    def updateSelectedObjectDescriptionFrameContent(self, clickedOnObject):
        for widget in self.selectedObjectDescriptionFrame.winfo_children():
            widget.destroy()
        if (clickedOnObject["type"] == "individual"):
            lblName = tk.Label(self.selectedObjectDescriptionFrame,
                               text="Object = Individual " + clickedOnObject["name"])
            lblHasReproduced = tk.Label(self.selectedObjectDescriptionFrame,
                    text="Has reproduced : " + str(clickedOnObject["hasReproduced"]))
            lblHasEaten = tk.Label(self.selectedObjectDescriptionFrame,
                    text="Has eaten : " + str(clickedOnObject["hasEaten"]))
        else:
            lblName = tk.Label(self.selectedObjectDescriptionFrame,
                               text="Object = Food")
        lblCoord = tk.Label(self.selectedObjectDescriptionFrame,
                text="Position : [" + str(clickedOnObject["startX"] / self.XCellSize)
                            + ", " + str(clickedOnObject["startY"] / self.YCellSize)
                            + "]")
        lblName.place(x=70,y=90)
        lblCoord.place(x=70,y=120)
        if (clickedOnObject["type"] == "individual"):
            lblHasReproduced.place(x=70,y=150)
            lblHasEaten.place(x=70,y=180)
        self.selectedObjectDescriptionFrame.pack()
        self.mainWindow.update()
        self.mainWindow.update_idletasks()

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

        self.createSelectedObjectDescriptionFrame()

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
                    self.updateSelectedObjectDescriptionFrameContent(clickedOnObject)
                prevMouseXClick = mouseXClick
                prevMouseYClick = mouseYClick
            self.mainWindow.update()


    def createSelectedObjectDescriptionFrame(self):
        self.selectedObjectDescriptionFrame = tk.Frame(self.mainWindow,
                                                       width=self.frameLength,
                                                       height=self.frameHeight)
        self.selectedObjectDescriptionFrame.pack(side=tk.RIGHT)
        self.mainWindow.update_idletasks()





def initGUIApplication(winWidth, winHeight, mapSizeX, mapSizeY):
    applicationGUI = ApplicationGUI(winWidth, winHeight, mapSizeX, mapSizeY)
    applicationGUI.createApplicationWindow()
    applicationGUI.createMapFrame()
    applicationGUI.createMap()
    return applicationGUI

