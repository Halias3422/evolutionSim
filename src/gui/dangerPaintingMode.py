import tkinter as tk

H1TITLEFONT = ("Arial", 20)
H2TITLEFONT = ("Arial", 18)
H3TITLEFONT = ("Arial", 16)
H4TITLEFONT = ("Arial", 14)

class DangerPaintingMenu:

    def __init__(self,applicationGUI, menusTabs, width, height):
        self.dangerPaintingFrame = tk.Frame(menusTabs,
                                            width=width,
                                            height=height)
        self.dangerPaintingFrame.grid_propagate(False)
        self.dangerPaintingFrame.grid_rowconfigure(0, weight=1)
        self.dangerPaintingFrame.grid_rowconfigure(1, weight=1)
        self.dangerPaintingFrame.grid_rowconfigure(2, weight=1)
        self.__createBrushSelectionFrame()
        self.__createBrushSizeFrame(applicationGUI)
        self.__createDangerCoverageFrame()

    def __createBrushSizeFrame(self, applicationGUI):
        self.brushSizeFrame = tk.LabelFrame(self.dangerPaintingFrame,
                         text=" Brush size ",
                         font=H2TITLEFONT,
                         labelanchor='n',
                         width=self.dangerPaintingFrame.winfo_reqwidth(),
                         height=self.dangerPaintingFrame.winfo_reqheight() / 3)
        self.brushSizeFrame.grid_propagate(False)
        self.brushSizeFrame.grid_columnconfigure(0, weight=1)
        self.brushSizeFrame.grid_columnconfigure(1, weight=1)
        self.brushSizeFrame.grid_columnconfigure(2, weight=1)
        self.brushSizeFrame.grid_columnconfigure(3, weight=1)
        self.brushSizeFrame.grid_rowconfigure(0, weight=1)
        self.brushSizeFrame.grid_rowconfigure(1, weight=1)
        self.brushSizeFrame.grid_rowconfigure(2, weight=1)
        self.brushSizeFrame.grid_rowconfigure(3, weight=1)
        self.brushSizeFrame.grid(row=1)
        self.lblBrushSizeX = tk.Label(self.brushSizeFrame,
                                      text="Length:    ",
                                      font=H3TITLEFONT)
        self.lblBrushSizeX.grid(column=1, row=1, sticky='e')
        self.brushSizeX = tk.IntVar(value=3)
        self.spbBrushSizeX = tk.Spinbox(self.brushSizeFrame,
                                        from_=1,
                                        to=100,
                                        increment=1,
                                        textvariable=self.brushSizeX,
                                        font=H3TITLEFONT,
                                        width=3)
        self.spbBrushSizeX.grid(column=2, row=1, sticky='w')
        self.lblBrushSizeY = tk.Label(self.brushSizeFrame,
                                      text="Height:    ",
                                      font=H3TITLEFONT)
        self.lblBrushSizeY.grid(column=1, row=2, sticky='e')
        self.brushSizeY = tk.IntVar(value=3)
        self.spbBrushSizeY = tk.Spinbox(self.brushSizeFrame,
                                        from_=1,
                                        to=100,
                                        increment=1,
                                        textvariable=self.brushSizeY,
                                        font=H3TITLEFONT,
                                        width=3)
        self.spbBrushSizeY.grid(column=2, row=2, sticky='w')



    def __createDangerCoverageFrame(self):
        self.dangerCoverageFrame = tk.LabelFrame(self.dangerPaintingFrame,
                         text=" Danger map coverage ",
                         font=H2TITLEFONT,
                         labelanchor='n',
                         width=self.dangerPaintingFrame.winfo_reqwidth(),
                         height=self.dangerPaintingFrame.winfo_reqheight() / 3)
        self.dangerCoverageFrame.grid_propagate(False)
        self.dangerCoverageFrame.grid_columnconfigure((0, 2), weight=1)
        self.dangerCoverageFrame.grid_rowconfigure((0, 2), weight=1)
        self.dangerCoverageFrame.grid(row=2)
        self.lblPlaceHolderDangerCoverage = tk.Label(self.dangerCoverageFrame,
                         text="Paint on map to add"
                             + " danger zones",
                         font=H3TITLEFONT)
        self.lblPlaceHolderDangerCoverage.grid_propagate(False)
        self.lblPlaceHolderDangerCoverage.grid(column=1, row=0)


    def __createBrushSelectionFrame(self):
        self.brushSelectionFrame = tk.LabelFrame(self.dangerPaintingFrame,
                         text=" Brush selection ",
                         font=H2TITLEFONT,
                         labelanchor='n',
                         width=self.dangerPaintingFrame.winfo_reqwidth(),
                         height=self.dangerPaintingFrame.winfo_reqheight() / 3)
        self.brushSelectionFrame.grid_propagate(False)
        self.brushSelectionFrame.grid_columnconfigure(0, weight=1)
        self.brushSelectionFrame.grid_columnconfigure(1, weight=1)
        self.brushSelectionFrame.grid_columnconfigure(2, weight=1)
        self.brushSelectionFrame.grid_columnconfigure(3, weight=1)
        self.brushSelectionFrame.grid_columnconfigure(4, weight=1)
        self.brushSelectionFrame.grid_rowconfigure((0, 4), weight=1)
        self.brushSelectionFrame.grid(row=0)
        self.__createSquareBrushFrame()
        self.__createRoundBrushFrame()

    def __createRoundBrushFrame(self):
        self.roundBrushFrame = tk.Frame(self.brushSelectionFrame,
                    width=int(self.brushSelectionFrame.winfo_reqwidth() / 5),
                    height=int((self.brushSelectionFrame.winfo_reqheight() / 5) * 3))
        self.roundBrushFrame.grid_propagate(False)
        self.roundBrushFrame.grid_columnconfigure(0, weight=1)
        self.roundBrushFrame.grid_rowconfigure(0, weight=1)
        self.roundBrushFrame.grid_rowconfigure(1, weight=1)
        self.roundBrushFrame.grid(column=3, columnspan=1, row=1, rowspan=3)
        self.roundBrushCanvas = tk.Canvas(self.roundBrushFrame,
                    bg="white",
                    highlightthickness=1,
                    highlightbackground="black",
                    width=self.brushCanvasSize,
                    height=self.brushCanvasSize)
        self.roundBrushCanvas.grid(row=0)
        self.rdbRoundBrush = tk.Radiobutton(self.roundBrushFrame,
                                            text="Round",
                                            value="roundBrush",
                                            variable=self.brushType,
                                             highlightthickness=0,
                                             width=self.brushCanvasSize,
                                            font=H3TITLEFONT)
        self.__fillRoundBrushCanvas()
        self.rdbRoundBrush.grid(row=1)


    def __createSquareBrushFrame(self):
        self.brushType = tk.StringVar(value="line")
        self.squareBrushFrame = tk.Frame(self.brushSelectionFrame,
                width=int(self.brushSelectionFrame.winfo_reqwidth() / 5),
                height=int((self.brushSelectionFrame.winfo_reqheight() / 5) * 3))
        self.squareBrushFrame.grid_propagate(False)
        self.squareBrushFrame.grid_columnconfigure(0, weight=1)
        self.squareBrushFrame.grid_rowconfigure(0, weight=1)
        self.squareBrushFrame.grid_rowconfigure(1, weight=1)
        self.squareBrushFrame.grid(column=1, columnspan=1, row=1, rowspan=3)
        self.__determineBrushCanvasSize()
        self.squareBrushCanvas = tk.Canvas(self.squareBrushFrame,
                                   bg="white",
                                   highlightthickness=1,
                                   highlightbackground="black",
                                   width=self.brushCanvasSize,
                                   height=self.brushCanvasSize)
        self.squareBrushCanvas.grid(row=0)
        self.__fillSquareBrushCanvas()
        self.rdbSquareBrush = tk.Radiobutton(self.squareBrushFrame,
                                             text="Line",
                                             value="line",
                                             variable=self.brushType,
                                             highlightthickness=0,
                                             width=self.brushCanvasSize,
                                             font=H3TITLEFONT)
        self.rdbSquareBrush.grid(row=1)

    def __determineBrushCanvasSize(self):
        self.brushCanvasSize = int((self.squareBrushFrame.winfo_reqheight() / 3 * 2))
        while (self.brushCanvasSize % 10 != 0):
            self.brushCanvasSize += 1

    def __fillSquareBrushCanvas(self):
        self.__drawOnBrushCanvas(self.squareBrushCanvas, 3, 3, 7, 7)
        self.__drawGridOnBrushCanvas(self.squareBrushCanvas)

    def __drawOnBrushCanvas(self, brushCanvas, startX, startY, endX, endY):
        XCellSize = brushCanvas.winfo_reqwidth() / 10
        YCellSize = brushCanvas.winfo_reqheight() / 10
        brushCanvas.create_rectangle(XCellSize * startX,
                                     YCellSize * startY,
                                     XCellSize * endX,
                                     YCellSize * endY,
                                     fill="orange")
    def __fillRoundBrushCanvas(self):
        self.__drawOnBrushCanvas(self.roundBrushCanvas, 3, 3, 7, 7)
        self.__drawOnBrushCanvas(self.roundBrushCanvas, 2, 4, 8, 6)
        self.__drawOnBrushCanvas(self.roundBrushCanvas, 4, 2, 6, 8)
        self.__drawGridOnBrushCanvas(self.roundBrushCanvas)

    def __drawGridOnBrushCanvas(self, brushCanvas):
        height = brushCanvas.winfo_reqheight()
        width = brushCanvas.winfo_reqwidth()
        currPosY = height
        while (currPosY >= 0):
            brushCanvas.create_line(0, currPosY, width, currPosY, fill="black")
            currPosY -= height / 10
        currPosX = width
        while (currPosX >= 0):
            brushCanvas.create_line(currPosX, 0, currPosX, height, fill="black")
            currPosX -= width / 10


def enterDangerPaintingMode(applicationGUI, event=None):
    pass
