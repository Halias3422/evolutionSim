import tkinter as tk
import keyboard
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

    def printFoodOnMap(self, foodList):
        for food in foodList:
            startX = food[1] * self.XCellSize
            startY = food[0] * self.YCellSize
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
                                       loopIndex, generationLifeSpan):
        self.map.delete("all")
        # self.__createMapGrid()
        if (loopIndex < generationLifeSpan):
            self.printPopulationOnMap(populationList, loopIndex)
            self.printFoodOnMap(foodList[loopIndex])
        else:
            self.printSurvivingIndividuals(populationList)
        self.map.pack()
        self.mainWindow.update()


    def printGenerationLifeSpanFrameByFrame(self, populationList, foodList,
                                            generationLifeSpan):
        loopIndex = 0
        print("press l to go forward, h to go backward or enter to quit")
        while (loopIndex <= generationLifeSpan):
            self.addContentForCurrentFrameToMap(populationList, foodList,
                                                loopIndex, generationLifeSpan)
            print("loop " + str(loopIndex))
            while True:
                event = keyboard.read_event()
                if (event.event_type == keyboard.KEY_DOWN):
                    if (event.name == 'l' and loopIndex < generationLifeSpan):
                        loopIndex += 1
                        break
                    elif (event.name == 'h'and loopIndex > 0):
                        loopIndex -= 1
                        break
                    elif (event.name == "esc"):
                        exit()
                    elif (event.name == "enter"):
                        loopIndex = generationLifeSpan
                        break


def initGUIApplication(winWidth, winHeight, mapSizeX, mapSizeY):
    applicationGUI = ApplicationGUI(winWidth, winHeight, mapSizeX, mapSizeY)
    applicationGUI.createApplicationWindow()
    applicationGUI.createMapFrame()
    applicationGUI.createMap()
    return applicationGUI
