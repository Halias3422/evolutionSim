import tkinter as tk
from tkinter import ttk
from .mainMenu import MainMenu
from .runInfoMenu import RunInfoMenu
from .dangerPaintingMode import DangerPaintingMenu

class Menus:

    def __init__(self, mainWindow, frameLength, frameHeight, runGenerationsLife,
                 applicationGUI):
        self.menusFrame = tk.Frame(mainWindow, width=frameLength,
                                   height=frameHeight)
        self.menusFrame.pack_propagate(False)
        self.menusFrame.pack()
        self.__createMenusTabs(mainWindow, frameLength, frameHeight)
        mainWindow.update_idletasks()

        self.dangerPaintingMenu = DangerPaintingMenu(applicationGUI,
                                                     self.menusTabs,
                                                     self.menusFrame.winfo_width(),
                                                     self.menusFrame.winfo_height())
        self.mainMenu = MainMenu(self.menusTabs, mainWindow,
                                 self.menusFrame.winfo_width(),
                                 self.menusFrame.winfo_height(),
                                 runGenerationsLife, applicationGUI)
        self.runInfoMenu = RunInfoMenu(self.menusTabs,
                                       self.menusFrame.winfo_width(),
                                       self.menusFrame.winfo_height())
        self.__addTabsToMenus()

    def __createMenusTabs(self, mainWindow, frameLength, frameHeight):
        self.menusTabs = ttk.Notebook(self.menusFrame)
        self.menusTabs.pack_propagate(False)
        self.menusTabs.pack()

    def __addTabsToMenus(self):
        pass
        self.menusTabs.add(self.mainMenu.menusFrame, text="New Run")
        self.menusTabs.add(self.runInfoMenu.runInfoFrame, text="Run Info")
        self.menusTabs.add(self.dangerPaintingMenu.dangerPaintingFrame, text="Painting")
        self.menusTabs.hide(self.runInfoMenu.runInfoFrame)

    def enableRunInfoTab(self):
        self.menusTabs.add(self.runInfoMenu.runInfoFrame)
