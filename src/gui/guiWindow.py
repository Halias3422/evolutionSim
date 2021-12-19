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


def initGUIApplication(winWidth, winHeight, runGenerationsLife):
    applicationGUI = ApplicationGUI(winWidth, winHeight)
    applicationGUI.createApplicationWindow()
    applicationGUI.createMainFrames(runGenerationsLife)
    applicationGUI.createMap(0, 0)
    return applicationGUI
