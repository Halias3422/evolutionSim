import tkinter as tk

class RunInfoMenu():

    def __init__(self, menusTabs, width, height):
        self.runInfoFrame = tk.LabelFrame(menusTabs,
                                          text="Currently selected Object info : ",
                                          width=width,
                                          height=height / 2)
        self.runInfoFrame.pack()
        self.__initRunInfoMenuContent()

    def __initRunInfoMenuContent(self):
        self.placeHolderText = tk.Label(self.runInfoFrame,
                                        text="Click on an object on the map to print its data")
