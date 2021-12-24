import tkinter as tk
from PIL import Image, ImageTk

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
        self.mouseX = 0
        self.mouseY = 0
        self.currHoveringPosition = [0, 0]
        self.prevHoveringPosition = [0, 0]

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
        self.donePainting = False
        self.btnDonePainting = tk.Button(self.dangerCoverageFrame,
                                         text=" Done ",
                                         font=("Arial", 32),
                                         bg="green",
                                         fg="white",
                                         command=lambda: self.__donePaintingDangerZones())
        self.btnDonePainting.grid(column=1, row=1)

    def __donePaintingDangerZones(self, event=None):
        print("LA")
        self.donePainting = True


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
                                            value="round",
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

    def __drawBrushOnMapCursorPosition(self, applicationGUI, event):
        self.mouseX = event.x
        self.mouseY = event.y
        self.currHoveringPosition = [int(event.y / applicationGUI.YCellSize),
                int(event.x / applicationGUI.XCellSize)]

    def __retreiveFocusPointForHoveringBrush(self):

        focusX = int(self.brushSizeX.get() / 2)
        focusY = int(self.brushSizeY.get() / 2)
        if (self.brushSizeX.get() % 2 != 0):
            focusX += 1
        if (self.brushSizeY.get() % 2 != 0):
            focusY += 1
        if (focusX == 0):
            focusX = 1
        if (focusY == 0):
            focusY = 1
        return focusX, focusY

    def __retreiveHoveringRectangleExtremities(self, applicationGUI, focusX,
                                               focusY):
        self.brushStartX = self.currHoveringPosition[1] - (focusX - 1)
        if (self.brushStartX < 0):
            self.brushStartX = 0
        self.brushStartX = self.brushStartX * applicationGUI.XCellSize

        self.brushStartY = self.currHoveringPosition[0] - (focusY - 1)
        if (self.brushStartY < 0):
            self.brushStartY = 0
        self.brushStartY = self.brushStartY * applicationGUI.YCellSize

        self.brushEndX = self.brushStartX + self.brushSizeX.get() * applicationGUI.XCellSize
        if (self.brushEndX > applicationGUI.frameLength):
            self.brushEndX = applicationGUI.frameLength
        self.brushEndY = self.brushStartY + self.brushSizeY.get() * applicationGUI.YCellSize
        if (self.brushEndY > applicationGUI.frameHeight):
            self.brushEndY = applicationGUI.frameHeight

    def __createHoveringRectangleForRoundOnMap(self, applicationGUI, **options):
        startX = self.brushStartX
        while (startX <= self.brushEndX):
            newPaintedLine = {
                    "startX": startX,
                    "endX": startX + applicationGUI.XCellSize,
                    "startY": self.brushStartY,
                    "endY": self.brushEndY
                    }
            if (newPaintedLine not in self.paintedCircleLines):
                print("la")
                applicationGUI.map.create_rectangle(startX, self.brushStartY,
                                                    startX + applicationGUI.XCellSize,
                                                    self.brushEndY,
                                                    tag="hoveringBrush",
                                                    **options)
                self.paintedCircleLines.append(newPaintedLine)
            startX += applicationGUI.XCellSize

    def __createHoveringRectangleOnMap(self, applicationGUI, **options):
        if ("alpha" in options):
            alpha = int(options.pop("alpha") * 255)
            fill = options.pop("fill")
            fill = applicationGUI.mainWindow.winfo_rgb(fill) + (alpha,)
            try:
                image = Image.new("RGBA", (int(self.brushEndX) - int(self.brushStartX),
                            int(self.brushEndY) - int(self.brushStartY)), fill)
            except:
                return
            self.images.append(ImageTk.PhotoImage(image))
            applicationGUI.map.create_image(self.brushStartX, self.brushStartY, image=self.images[-1], anchor='nw')
            if (self.brushType.get() == "round"):
                self.__createHoveringRectangleForRoundOnMap(applicationGUI, **options)
            else:
                print("laaaa")
                applicationGUI.map.create_rectangle(self.brushStartX, self.brushStartY,
                                                    self.brushEndX, self.brushEndY,
                                                    tag="hoveringBrush",
                                                    **options)

    def __printHoveringLineBrushOnMap(self, applicationGUI):
        focusX, focusY = self.__retreiveFocusPointForHoveringBrush()
        self.__retreiveHoveringRectangleExtremities(applicationGUI, focusX, focusY)
        self.images = []
        self.__createHoveringRectangleOnMap(applicationGUI,fill="orange", alpha=.5)


    def __printCircleOnMap(self, applicationGUI, circleCenterX, circleCenterY,
                            currX, currY):
        self.brushStartX = (circleCenterX - currX - 1) * applicationGUI.XCellSize
        self.brushEndX = (circleCenterX + currX + 1) * applicationGUI.XCellSize
        self.brushStartY = (circleCenterY + currY) * applicationGUI.YCellSize
        self.brushEndY = (circleCenterY + currY + 1) * applicationGUI.YCellSize
        self.__createHoveringRectangleOnMap(applicationGUI, fill="orange", alpha=.5)
        self.brushStartY = (circleCenterY - currY - 1) * applicationGUI.YCellSize
        self.brushEndY = (circleCenterY - currY) * applicationGUI.YCellSize
        self.__createHoveringRectangleOnMap(applicationGUI, fill="orange", alpha=.5)
        self.brushStartX = (circleCenterX - currY - 1) * applicationGUI.XCellSize
        self.brushEndX = (circleCenterX + currY + 1) * applicationGUI.XCellSize
        self.brushStartY = (circleCenterY + currX) * applicationGUI.YCellSize
        self.brushEndY = (circleCenterY + currX + 1) * applicationGUI.YCellSize
        self.__createHoveringRectangleOnMap(applicationGUI, fill="orange", alpha=.5)
        self.brushStartY = (circleCenterY - currX - 1) * applicationGUI.YCellSize
        self.brushEndY = (circleCenterY - currX) * applicationGUI.YCellSize
        self.__createHoveringRectangleOnMap(applicationGUI, fill="orange", alpha=.5)

    def __createHoveringCircleOnMap(self, applicationGUI, circleCenterX, circleCenterY,
                                    circleRadius):
        self.images = []
        self.paintedCircleLines = []
        currX = 0
        currY = circleRadius
        currD = 3 - 2 * circleRadius
        self.__printCircleOnMap(applicationGUI, circleCenterX, circleCenterY,
                                currX, currY)
        while (currY >= currX):
            if (currD >= 0):
                currD = currD + (4 * currX) - (4 * currY) + 10
                currY -= 1
            else:
                currD = currD + 4 * currX + 6
            currX += 1
            self.__printCircleOnMap(applicationGUI, circleCenterX, circleCenterY,
                                    currX, currY)
        print(self.paintedCircleLines)


    # bresenham-s circle algorithm
    def __printHoveringRoundBrushOnMap(self, applicationGUI):
        focusX, focusY = self.__retreiveFocusPointForHoveringBrush()
        self.__retreiveHoveringRectangleExtremities(applicationGUI, focusX, focusY)
        circleCenterX = self.currHoveringPosition[1]
        circleCenterY = self.currHoveringPosition[0]
        circleRadius = focusX
        self.__createHoveringCircleOnMap(applicationGUI, circleCenterX, circleCenterY,
                                         circleRadius)


    def __printHoveringBrushOnMap(self, applicationGUI):
        applicationGUI.map.delete("hoveringBrush")
        if (self.brushType.get() == "line"):
            self.__printHoveringLineBrushOnMap(applicationGUI)
        elif (self.brushType.get() == "round"):
            self.__printHoveringRoundBrushOnMap(applicationGUI)

    def __clickInsertBrushOnMap(self, applicationGUI, mainData):
        newDangerZone = {
                "startX": self.brushStartX,
                "startY": self.brushStartY,
                "endX": self.brushEndX,
                "endY": self.brushEndY
                }
        self.addedDangerZones.append(newDangerZone)
        applicationGUI.map.delete("all")
        for rectangle in self.addedDangerZones:
            applicationGUI.map.create_rectangle(rectangle["startX"],
                                                rectangle["startY"],
                                                rectangle["endX"],
                                                rectangle["endY"],
                                                fill="orange",
                                                tag="dangerZone")
        applicationGUI.createMapGrid(mainData.mapSizeX, mainData.mapSizeY)


    def __triggerAddingBrushOnMap(self, event=None):
        self.mouseButtonPressed = True

    def __triggerStopAddingBrushOnMap(self, event=None):
        self.mouseButtonPressed = False

    def addDangerZonesToMap(self, applicationGUI, mainData):
        self.mouseButtonPressed = False
        self.dangerPaintingFrame.grid()
        self.addedDangerZones = []
        applicationGUI.menus.enableDangerPaintingTab()
        applicationGUI.menus.menusTabs.select(self.dangerPaintingFrame)
        self.spbBrushSizeY["to"] = mainData.mapSizeY
        self.spbBrushSizeX["to"] = mainData.mapSizeX
        applicationGUI.createMapGrid(mainData.mapSizeX, mainData.mapSizeY)
        applicationGUI.mainWindow.update()
        applicationGUI.map.bind("<Motion>",
            lambda event, arg=applicationGUI: self.__drawBrushOnMapCursorPosition(arg, event))
        applicationGUI.map.bind("<ButtonPress-1>",
                self.__triggerAddingBrushOnMap)
            # lambda event, arg=applicationGUI, arg2=mainData: self.__clickInsertBrushOnMap(arg, arg2, event))
        applicationGUI.map.bind("<ButtonRelease-1>",
                self.__triggerStopAddingBrushOnMap)
        while (True):
            if (self.mouseButtonPressed is True):
                self.__clickInsertBrushOnMap(applicationGUI,mainData)
            if (self.prevHoveringPosition != self.currHoveringPosition):
                self.__printHoveringBrushOnMap(applicationGUI)
                self.prevHoveringPosition = self.currHoveringPosition
            if (self.donePainting is True):
                print("breaaak")
                break
            applicationGUI.mainWindow.update()



