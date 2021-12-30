import tkinter as tk
from PIL import Image, ImageTk, ImageColor

H1TITLEFONT = ("Arial", 20)
H2TITLEFONT = ("Arial", 18)
H3TITLEFONT = ("Arial", 16)
H4TITLEFONT = ("Arial", 14)

class DangerPaintingMenu:
    def __init__(self,applicationGUI, menusTabs, width, height):
        self.brushColor = "orange"
        self.dangerPaintingFrame = tk.Frame(menusTabs,
                                            width=width,
                                            height=height)
        self.dangerPaintingFrame.grid_propagate(False)
        self.dangerPaintingFrame.grid_rowconfigure(0, weight=1)
        self.dangerPaintingFrame.grid_rowconfigure(1, weight=1)
        self.dangerPaintingFrame.grid_rowconfigure(2, weight=1)
        self.dangerPaintingFrame.grid_columnconfigure(0, weight=1)
        self.__createBrushSelectionFrame()
        self.__createMapCoverageFrame()
        self.__createDonePaintingFrame()
        self.mouseX = 0
        self.mouseY = 0
        self.currHoveringPosition = [0, 0]
        self.prevHoveringPosition = [0, 0]


    def __donePaintingDangerZones(self, event=None):
        self.donePainting = True

    def __createDonePaintingFrame(self):
        self.donePainting = False
        self.donePaintingFrame = tk.LabelFrame(self.dangerPaintingFrame,
                         width=self.dangerPaintingFrame.winfo_reqwidth(),
                         height=int(self.dangerPaintingFrame.winfo_reqheight() / 3))
        self.donePaintingFrame.grid_propagate(False)
        self.donePaintingFrame.grid_columnconfigure(0, weight=1)
        self.donePaintingFrame.grid_columnconfigure(1, weight=1)
        self.donePaintingFrame.grid_columnconfigure(2, weight=1)
        self.donePaintingFrame.grid_rowconfigure(0, weight=1)
        self.donePaintingFrame.grid_rowconfigure(1, weight=1)
        self.donePaintingFrame.grid_rowconfigure(2, weight=1)
        self.donePaintingFrame.grid(column=0, row=2)
        self.btnDonePainting = tk.Button(self.donePaintingFrame,
                                         text="   Done   ",
                                         font=("Arial", 64),
                                         bg="green",
                                         fg="white",
                                         command=lambda: self.__donePaintingDangerZones())
        self.btnDonePainting.grid(column=1, row=1)

    def __createMapCoverageFrame(self):
        self.mapCoverageFrame = tk.LabelFrame(self.dangerPaintingFrame,
                         text=" Map coverage ",
                         font=H1TITLEFONT,
                         labelanchor='n',
                         width=self.dangerPaintingFrame.winfo_reqwidth(),
                         height=int(self.dangerPaintingFrame.winfo_reqheight() / 3))
        self.mapCoverageFrame.grid_propagate(False)
        self.mapCoverageFrame.grid_columnconfigure(0, weight=1)
        self.mapCoverageFrame.grid_columnconfigure(1, weight=1)
        self.mapCoverageFrame.grid_columnconfigure(2, weight=1)
        self.mapCoverageFrame.grid_columnconfigure(3, weight=1)
        self.mapCoverageFrame.grid_rowconfigure(0, weight=1)
        self.mapCoverageFrame.grid(column=0, row=1)
        self.populationCoverageFrame = \
                self.__createMapCoverageSubFrames(" Population ", 0)
        self.dangerCoverageFrame = \
                self.__createMapCoverageSubFrames(" Danger ", 1)
        self.obstacleCoverageFrame = \
                self.__createMapCoverageSubFrames(" Obstacles ", 2)
        self.foodCoverageFrame = \
                self.__createMapCoverageSubFrames(" Food ", 3)


    def __createMapCoverageSubFrames(self, frameText, frameColumn):
        subFrame = tk.LabelFrame(self.mapCoverageFrame,
                         text=frameText,
                         font=H2TITLEFONT,
                         labelanchor='n',
                         width=int(self.mapCoverageFrame.winfo_reqwidth() / 4),
                         height=self.mapCoverageFrame.winfo_reqheight())
        subFrame.grid(column=frameColumn, row=0)
        return subFrame

    def __createBrushSelectionFrame(self):
        self.brushSelectionFrame = tk.LabelFrame(self.dangerPaintingFrame,
                         text=" Brush ",
                         font=H1TITLEFONT,
                         labelanchor='n',
                         width=self.dangerPaintingFrame.winfo_reqwidth(),
                         height=int(self.dangerPaintingFrame.winfo_reqheight() / 3))
        self.brushSelectionFrame.grid_propagate(False)
        self.brushSelectionFrame.grid_columnconfigure(0, weight=1)
        self.brushSelectionFrame.grid_columnconfigure(1, weight=1)
        self.brushSelectionFrame.grid_columnconfigure(2, weight=1)
        self.brushSelectionFrame.grid_rowconfigure(0, weight=1)
        self.brushSelectionFrame.grid(column=0, row=0)
        self.__createBrushTypeFrame()
        self.__createBrushStyleFrame()
        self.__createBrushSizeFrame()

    def __createBrushTypeFrame(self):
        self.brushType = tk.StringVar(value="danger")
        self.brushTypeFrame = tk.LabelFrame(self.brushSelectionFrame,
                             text=" Type ",
                             font=H2TITLEFONT,
                             labelanchor='n',
                             width=self.brushSelectionFrame.winfo_reqwidth() / 3,
                             height=self.brushSelectionFrame.winfo_reqheight())
        self.brushTypeFrame.grid_propagate(False)
        self.brushTypeFrame.grid_columnconfigure(0, weight=1)
        self.brushTypeFrame.grid_columnconfigure(1, weight=1)
        self.brushTypeFrame.grid_columnconfigure(2, weight=1)
        self.brushTypeFrame.grid_rowconfigure(0, weight=1)
        self.brushTypeFrame.grid_rowconfigure(1, weight=1)
        self.brushTypeFrame.grid_rowconfigure(2, weight=1)
        self.brushTypeFrame.grid_rowconfigure(3, weight=1)
        self.brushTypeFrame.grid_rowconfigure(4, weight=1)
        self.brushTypeFrame.grid(column=0, row=0)
        self.rdbPopulationPainting = tk.Radiobutton(self.brushTypeFrame,
                                    text="Population",
                                    font=H3TITLEFONT,
                                    value="population",
                                    variable=self.brushType,
                                    highlightthickness=0)
        self.rdbPopulationPainting.grid(column=1, row=0, sticky='w')
        self.rdbDangerPainting = tk.Radiobutton(self.brushTypeFrame,
                                    text="Danger",
                                    font=H3TITLEFONT,
                                    value="danger",
                                    variable=self.brushType,
                                    highlightthickness=0)
        self.rdbDangerPainting.grid(column=1, row=1, sticky='w')
        self.rdbObstaclePainting = tk.Radiobutton(self.brushTypeFrame,
                                    text="Obstacle",
                                    font=H3TITLEFONT,
                                    value="obstacle",
                                    variable=self.brushType,
                                    highlightthickness=0)
        self.rdbObstaclePainting.grid(column=1, row=2, sticky='w')
        self.rdbFoodPainting = tk.Radiobutton(self.brushTypeFrame,
                                    text="Food",
                                    font=H3TITLEFONT,
                                    value="food",
                                    variable=self.brushType,
                                    highlightthickness=0)
        self.rdbFoodPainting.grid(column=1, row=3, sticky='w')
        self.rdbEraserPainting = tk.Radiobutton(self.brushTypeFrame,
                                    text="Eraser",
                                    font=H3TITLEFONT,
                                    value="eraser",
                                    variable=self.brushType,
                                    highlightthickness=0)
        self.rdbEraserPainting.grid(column=1, row=4, sticky='w')



    def __createBrushStyleFrame(self):
        self.brushStyleFrame = tk.LabelFrame(self.brushSelectionFrame,
                             text=" Style ",
                             font=H2TITLEFONT,
                             labelanchor='n',
                             width=self.brushSelectionFrame.winfo_reqwidth() / 3,
                             height=self.brushSelectionFrame.winfo_reqheight())
        self.brushStyleFrame.grid_propagate(False)
        self.brushStyleFrame.grid_columnconfigure(0, weight=1)
        self.brushStyleFrame.grid_rowconfigure(0, weight=1)
        self.brushStyleFrame.grid_rowconfigure(1, weight=1)
        self.brushStyleFrame.grid(column=1, row=0)
        self.__createSquareBrushFrame()
        self.__createRoundBrushFrame()

    def __createBrushSizeFrame(self):
        self.brushSizeFrame = tk.LabelFrame(self.brushSelectionFrame,
                             text=" Size ",
                             font=H2TITLEFONT,
                             labelanchor='n',
                             width=self.brushSelectionFrame.winfo_reqwidth() / 3,
                             height=self.brushSelectionFrame.winfo_reqheight())
        self.brushSizeFrame.grid_propagate(False)
        self.brushSizeFrame.grid_columnconfigure(0, weight=1)
        self.brushSizeFrame.grid_columnconfigure(1, weight=1)
        self.brushSizeFrame.grid_columnconfigure(2, weight=1)
        self.brushSizeFrame.grid_rowconfigure(0, weight=1)
        self.brushSizeFrame.grid_rowconfigure(1, weight=1)
        self.brushSizeFrame.grid_rowconfigure(2, weight=1)
        self.brushSizeFrame.grid_rowconfigure(3, weight=1)
        self.brushSizeFrame.grid_rowconfigure(4, weight=1)
        self.brushSizeFrame.grid_rowconfigure(5, weight=1)
        self.brushSizeFrame.grid_rowconfigure(6, weight=1)
        self.brushSizeFrame.grid(column=2, row=0)
        self.brushSizeX = tk.IntVar(value=3)
        self.brushSizeY = tk.IntVar(value=3)
        self.lblBrushSizeX = tk.Label(self.brushSizeFrame,
                                      text="Length:",
                                      font=H3TITLEFONT)
        self.lblBrushSizeX.grid(column=1, row=1)
        self.spbBrushSizeX = tk.Spinbox(self.brushSizeFrame,
                                        from_=1,
                                        to=100,
                                        increment=1,
                                        textvariable=self.brushSizeX,
                                        font=H3TITLEFONT,
                                        width=4)
        self.spbBrushSizeX.grid(column=1, row=2)
        self.lblBrushSizeY = tk.Label(self.brushSizeFrame,
                                      text="Height:",
                                      font=H3TITLEFONT)
        self.lblBrushSizeY.grid(column=1, row=4)
        self.spbBrushSizeY = tk.Spinbox(self.brushSizeFrame,
                                        from_=1,
                                        to=100,
                                        increment=1,
                                        textvariable=self.brushSizeY,
                                        font=H3TITLEFONT,
                                        width=4)
        self.spbBrushSizeY.grid(column=1, row=5)


    def __createRoundBrushFrame(self):
        self.roundBrushFrame = tk.Frame(self.brushStyleFrame,
                    width=self.brushSelectionFrame.winfo_reqwidth(),
                    height=int(self.brushSelectionFrame.winfo_reqheight() / 3))
        self.roundBrushFrame.grid_propagate(False)
        self.roundBrushFrame.grid_columnconfigure(0, weight=1)
        self.roundBrushFrame.grid_rowconfigure(0, weight=1)
        self.roundBrushFrame.grid_rowconfigure(1, weight=1)
        self.roundBrushFrame.grid(column=0, row=1)
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
                                            variable=self.brushStyle,
                                             highlightthickness=0,
                                            font=H3TITLEFONT)
        self.__fillRoundBrushCanvas()
        self.rdbRoundBrush.grid(row=1)


    def __createSquareBrushFrame(self):
        self.brushStyle = tk.StringVar(value="line")
        self.squareBrushFrame = tk.Frame(self.brushStyleFrame,
                width=self.brushStyleFrame.winfo_reqwidth(),
                height=int(self.brushStyleFrame.winfo_reqheight() / 3))
        self.squareBrushFrame.grid_propagate(False)
        self.squareBrushFrame.grid_columnconfigure(0, weight=1)
        self.squareBrushFrame.grid_rowconfigure(0, weight=1)
        self.squareBrushFrame.grid_rowconfigure(1, weight=1)
        self.squareBrushFrame.grid(column=0, row=0)
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
                                             variable=self.brushStyle,
                                             highlightthickness=0,
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
                                     fill=self.brushColor)
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

    def __createHoveringRectangleOnMap(self, applicationGUI, **options):
        if ("alpha" in options):
            alpha = int(options.pop("alpha") * 255)
            fill = options.pop("fill")
            if (fill == "orange"):
                fill = (255, 165, 0, 127)
            elif (fill == "black"):
                fill = (0, 0, 0, 127)
            elif (fill == "chocolate"):
                fill = (165, 42, 42, 127)
            elif (fill == "green"):
                fill = (0, 128, 0, 127)
            elif (fill == "grey"):
                fill = (128, 128, 128, 127)
            try:
                image = Image.new("RGBA", (int(self.brushEndX) - int(self.brushStartX),
                            int(self.brushEndY) - int(self.brushStartY)), fill)
                self.images.append(ImageTk.PhotoImage(image))
            except:
                return
            applicationGUI.map.create_image(self.brushStartX, self.brushStartY, image=self.images[-1], anchor='nw')

    def __printHoveringLineBrushOnMap(self, applicationGUI):
        focusX, focusY = self.__retreiveFocusPointForHoveringBrush()
        self.__retreiveHoveringRectangleExtremities(applicationGUI, focusX, focusY)
        self.images = []
        self.__createHoveringRectangleOnMap(applicationGUI,fill=self.brushColor, alpha=.5)

    def __registerCircleHoveringLines(self, startX, endX, startY, endY,
                                      applicationGUI):
        newLine = {
                "startX": startX,
                "endX": endX,
                "startY":startY,
                "endY":endY
                }
        lineRegisterUpdated = False
        for line in self.registeredCircleLines:
            if (line["startY"] == newLine["startY"] and
                    line["endY"] == newLine["endY"]):
                lineRegisterUpdated = True
                if (newLine["startX"] < line["startX"]):
                    line["startX"] = newLine["startX"]
                if (newLine["endX"] > line["endX"]):
                    line["endX"] = newLine["endX"]
        if (lineRegisterUpdated is False):
            self.registeredCircleLines.append(newLine)

    def __constructCircleLines(self, applicationGUI, circleCenterX, circleCenterY,
                            currX, currY):
        startX = (circleCenterX - currX - 1) * applicationGUI.XCellSize
        endX = (circleCenterX + currX + 1) * applicationGUI.XCellSize
        startY = (circleCenterY + currY) * applicationGUI.YCellSize
        endY = (circleCenterY + currY + 1) * applicationGUI.YCellSize
        self.__registerCircleHoveringLines(startX, endX, startY, endY, applicationGUI)
        startY = (circleCenterY - currY - 1) * applicationGUI.YCellSize
        endY = (circleCenterY - currY) * applicationGUI.YCellSize
        self.__registerCircleHoveringLines(startX, endX, startY, endY, applicationGUI)
        startX = (circleCenterX - currY - 1) * applicationGUI.XCellSize
        endX = (circleCenterX + currY + 1) * applicationGUI.XCellSize
        startY = (circleCenterY + currX) * applicationGUI.YCellSize
        endY = (circleCenterY + currX + 1) * applicationGUI.YCellSize
        self.__registerCircleHoveringLines(startX, endX, startY, endY, applicationGUI)
        startY = (circleCenterY - currX - 1) * applicationGUI.YCellSize
        endY = (circleCenterY - currX) * applicationGUI.YCellSize
        self.__registerCircleHoveringLines(startX, endX, startY, endY, applicationGUI)

    def __printHoveringCircleOnMap(self, applicationGUI):
        for line in self.registeredCircleLines:
            self.brushStartX = line["startX"]
            self.brushEndX = line["endX"]
            self.brushStartY = line["startY"]
            self.brushEndY = line["endY"]
            self.__createHoveringRectangleOnMap(applicationGUI, fill=self.brushColor, alpha=.5)

    def __createHoveringCircleOnMap(self, applicationGUI, circleCenterX, circleCenterY,
                                    circleRadius):
        self.images = []
        self.alreadyPrintedCells = []
        self.registeredCircleLines = []
        currX = 0
        currY = circleRadius
        currD = 3 - 2 * circleRadius
        self.__constructCircleLines(applicationGUI, circleCenterX, circleCenterY,
                                currX, currY)
        while (currY >= currX):
            if (currD >= 0):
                currD = currD + (4 * currX) - (4 * currY) + 10
                currY -= 1
            else:
                currD = currD + 4 * currX + 6
            currX += 1
            self.__constructCircleLines(applicationGUI, circleCenterX, circleCenterY,
                                    currX, currY)
        self.__printHoveringCircleOnMap(applicationGUI)


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
        if (self.brushStyle.get() == "line"):
            self.__printHoveringLineBrushOnMap(applicationGUI)
        elif (self.brushStyle.get() == "round"):
            self.__printHoveringRoundBrushOnMap(applicationGUI)


    def __clickDrawRectangleZone(self, applicationGUI):
        brushType = self.brushType.get()
        newZone = {
                "startX": self.brushStartX,
                "startY": self.brushStartY,
                "endX": self.brushEndX,
                "endY": self.brushEndY,
                "type": brushType
                }
        self.addedZones.append(newZone)
        self.__updateMapRepresentation(newZone, brushType, applicationGUI)

    def __clickDrawCircleZone(self, applicationGUI):
        brushType = self.brushType.get()
        for line in self.registeredCircleLines:
            newZone = {
                    "startX": line["startX"],
                    "startY": line["startY"],
                    "endX": line["endX"],
                    "endY": line["endY"],
                    "type": brushType
                    }
            self.addedZones.append(newZone)
            self.__updateMapRepresentation(newZone, brushType, applicationGUI)


    def __clickInsertBrushOnMap(self, applicationGUI, mainData):
        if (self.brushStyle.get() == "line"):
            self.__clickDrawRectangleZone(applicationGUI)
        elif (self.brushStyle.get() == "round"):
            self.__clickDrawCircleZone(applicationGUI)
        applicationGUI.map.delete("all")
        for zone in self.addedZones:
            color = "white"
            if (zone["type"] == "danger"):
                color = "orange"
            elif (zone["type"] == "population"):
                color = "black"
            elif (zone["type"] == "obstacle"):
                color = "chocolate"
            elif (zone["type"] == "food"):
                color = "green"
            applicationGUI.map.create_rectangle(zone["startX"],
                                                zone["startY"],
                                                zone["endX"],
                                                zone["endY"],
                                                fill=color,
                                                tag=zone["type"] + "Zone")
        applicationGUI.createMapGrid(mainData.mapSizeX, mainData.mapSizeY)


    def __triggerAddingBrushOnMap(self, event=None):
        self.mouseButtonPressed = True

    def __triggerStopAddingBrushOnMap(self, event=None):
        self.mouseButtonPressed = False

    def __changeCurrentBrushTypeStyle(self):
        currBrushType = self.brushType.get()
        if (currBrushType == "population"):
            self.brushColor = "black"
            self.__fillSquareBrushCanvas()
            self.__fillRoundBrushCanvas()
        elif (currBrushType == "danger"):
            self.brushColor = "orange"
            self.__fillSquareBrushCanvas()
            self.__fillRoundBrushCanvas()
        elif (currBrushType == "obstacle"):
            self.brushColor = "chocolate"
            self.__fillSquareBrushCanvas()
            self.__fillRoundBrushCanvas()
        elif (currBrushType == "food"):
            self.brushColor = "green"
            self.__fillSquareBrushCanvas()
            self.__fillRoundBrushCanvas()
        elif (currBrushType == "eraser"):
            self.brushColor = "grey"
            self.__fillSquareBrushCanvas()
            self.__fillRoundBrushCanvas()

    def __updateMapRepresentation(self, newZone, brushType, applicationGUI):
        currBrushType = brushType
        if (brushType == "eraser"):
            currBrushType = "empty"
        startX = int(newZone["startX"] / applicationGUI.XCellSize)
        endX = int(newZone["endX"] / applicationGUI.XCellSize)
        startY = int(newZone["startY"] / applicationGUI.YCellSize)
        endY = int(newZone["endY"] / applicationGUI.YCellSize)
        while (startY < endY):
            tmpStartX = startX
            while (tmpStartX < endX):
                if (startY >= 0 and startY < len(self.mapZonesRepresentation)
                        and tmpStartX >= 0 and tmpStartX < len(self.mapZonesRepresentation[0])):
                    self.mapZonesRepresentation[startY][tmpStartX] = currBrushType
                tmpStartX += 1
            startY += 1

    def __createMapZonesRepresentation(self, mainData):
        self.mapZonesRepresentation = [["empty" for x in range(mainData.mapSizeX)]\
                for y in range(mainData.mapSizeY)]

    def addDangerZonesToMap(self, applicationGUI, mainData):
        self.mouseButtonPressed = False
        self.dangerPaintingFrame.grid()
        self.addedZones = []
        self.__createMapZonesRepresentation(mainData)
        applicationGUI.menus.enableDangerPaintingTab()
        applicationGUI.menus.menusTabs.select(self.dangerPaintingFrame)
        self.spbBrushSizeY["to"] = mainData.mapSizeY
        self.spbBrushSizeX["to"] = mainData.mapSizeX
        applicationGUI.createMapGrid(mainData.mapSizeX, mainData.mapSizeY)
        applicationGUI.mainWindow.update()
        applicationGUI.map.bind("<Motion>",
            lambda event, arg=applicationGUI: self.__drawBrushOnMapCursorPosition(arg, event))
        applicationGUI.map.bind("<ButtonPress-1>", self.__triggerAddingBrushOnMap)
        applicationGUI.map.bind("<ButtonRelease-1>", self.__triggerStopAddingBrushOnMap)
        currBrushType = self.brushType.get()
        while (True):
            if (currBrushType != self.brushType.get()):
                self.__changeCurrentBrushTypeStyle()
                currBrushType = self.brushType.get()
            if (self.mouseButtonPressed is True):
                self.__clickInsertBrushOnMap(applicationGUI,mainData)
            if (self.prevHoveringPosition != self.currHoveringPosition):
                self.__printHoveringBrushOnMap(applicationGUI)
                self.prevHoveringPosition = self.currHoveringPosition
            if (self.donePainting is True):
                break
            if (applicationGUI.exiting == True):
                exit()
            applicationGUI.mainWindow.update()



