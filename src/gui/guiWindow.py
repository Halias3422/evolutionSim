import tkinter as tk
from debug.print import *

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

    def createMap(self):
        self.map = tk.Canvas(self.mapFrame, bg="white",
                             width=self.frameLength,
                             height=self.frameHeight)
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

    def printPopulationOnMap(self, populationList, loopIndex):
        for individual in populationList:
            startX = individual.mapPosition[loopIndex][1] * self.XCellSize
            startY = individual.mapPosition[loopIndex][0] * self.YCellSize
            self.map.create_rectangle(startX,
                                      startY,
                                      startX + self.XCellSize,
                                      startY + self.YCellSize,
                                      fill="red")

    def printFoodOnMap(self, foodList):
        for food in foodList:
            startX = food[1] * self.XCellSize
            startY = food[0] * self.YCellSize
            self.map.create_rectangle(startX,
                                      startY,
                                      startX + self.XCellSize,
                                      startY + self.YCellSize,
                                      fill="green")

    def printGenerationLifeSpanFrameByFrame(self, populationList, foodList,
                                            generationLifeSpan):
        input("BEGIN")
        loopIndex = 0
        while (loopIndex < generationLifeSpan):
            self.map.delete("all")
            # self.__createMapGrid()
            self.printPopulationOnMap(populationList, loopIndex)
            self.printFoodOnMap(foodList)
            self.map.pack()
            loopIndex += 1
            self.mainWindow.update()
            input("Press ENTER (loop " + str(loopIndex) + ")")


def initGUIApplication(winWidth, winHeight, mapSizeX, mapSizeY):
    applicationGUI = ApplicationGUI(winWidth, winHeight, mapSizeX, mapSizeY)
    applicationGUI.createApplicationWindow()
    applicationGUI.createMapFrame()
    applicationGUI.createMap()
    return applicationGUI
