import tkinter as tk

H1TITLEFONT = ("Arial", 20)
H2TITLEFONT = ("Arial", 18)
H3TITLEFONT = ("Arial", 16)
H4TITLEFONT = ("Arial", 14)

class RunInfoMenu():

    def __init__(self, menusTabs, width, height):
        self.runInfoFrame = tk.Frame(menusTabs,
                                     width=width,
                                     height=height)
        self.runInfoFrame.grid_propagate(False)
        self.runInfoFrame.pack()
        self.runInfoFrame.grid_columnconfigure(0, weight=1)
        self.runInfoFrame.grid_columnconfigure(1, weight=1)
        self.runInfoFrame.grid_rowconfigure(0, weight=1)
        self.runInfoFrame.grid_rowconfigure(1, weight=1)
        self.runInfoFrame.grid_rowconfigure(2, weight=1)
        self.__initRunInfoMenuContent()

    def __initRunInfoMenuContent(self):
        self.__initSelectedObjectInfoFrame()
        self.__initGlobalPopulationInfoFrame()
        self.__initProgressBarsFrame()

    def __initGlobalPopulationInfoFrame(self):
        self.globalPopulationInfoFrame = tk.LabelFrame(self.runInfoFrame,
                            text="Population info : ",
                            labelanchor='n',
                            font=H1TITLEFONT,
                            width=self.runInfoFrame.winfo_reqwidth(),
                            height=(self.runInfoFrame.winfo_reqheight() / 12) * 3)
        self.globalPopulationInfoFrame.grid_propagate(False)
        self.globalPopulationInfoFrame.grid_columnconfigure(0, weight=1)
        index = 0
        while (index < 5):
            self.globalPopulationInfoFrame.grid_rowconfigure(index, weight=1)
            index += 1
        self.globalPopulationInfoFrame.grid(column=0, columnspan=2, row=1)
        self.totalPopulationInfo = tk.Label(self.globalPopulationInfoFrame,                                                              font=H3TITLEFONT)
        self.totalPopulationInfo.grid(column=0, row=1)
        self.populationHasEatenInfo = tk.Label(self.globalPopulationInfoFrame,                                                               font=H3TITLEFONT)
        self.populationHasEatenInfo.grid(column=0, row=2)
        self.populationHasReproducedInfo = tk.Label(self.globalPopulationInfoFrame,                                                              font=H3TITLEFONT)
        self.populationHasReproducedInfo.grid(column=0, row=3)


    def __initSelectedObjectInfoFrame(self):
        self.objectInfoFrame = tk.LabelFrame(self.runInfoFrame,
                          text="Currently selected Object info : ",
                          labelanchor='n',
                          font=H1TITLEFONT,
                          width=self.runInfoFrame.winfo_reqwidth(),
                          height=(self.runInfoFrame.winfo_reqheight() / 12) * 5)
        self.objectInfoFrame.grid_propagate(False)
        self.objectInfoFrame.grid(column=0, columnspan=2, row=0)
        self.objectInfoFrame.grid_columnconfigure(0, weight=1)
        self.objectInfoFrame.grid_columnconfigure(1, weight=1)
        self.objectInfoFrame.grid_rowconfigure(0, weight=1)
        self.objectInfoFrame.grid_rowconfigure(1, weight=1)
        self.objectInfoFrame.grid_rowconfigure(2, weight=1)
        self.placeHolderText = tk.Label(self.objectInfoFrame,
                                        text="Click on an object on the map "\
                                                "to print its data",
                                        font=H3TITLEFONT)
        self.placeHolderText.grid(column=0, columnspan=2, row=1, sticky=tk.N)
        self.__initShowingIndividualInfo()

    def __initShowingIndividualInfo(self):
        self.individualInfoFrame = tk.LabelFrame(self.objectInfoFrame,
                                            labelanchor='n',
                                            font=H2TITLEFONT,
                                            width=self.objectInfoFrame.winfo_reqwidth() / 2,
                                            height=self.objectInfoFrame.winfo_reqheight())
        self.individualInfoFrame.grid_propagate(False)
        i = 0
        while (i < 5):
            self.individualInfoFrame.grid_rowconfigure(i, weight=1)
            i += 1
        self.individualInfoFrame.grid_columnconfigure(0, weight=1)
        self.individualInfoFrame.grid(column=0, row=0, rowspan=3)
        self.individualGenePoolFrame = tk.LabelFrame(self.objectInfoFrame,
                                                     text="Gene pool: ",
                                                     font=H2TITLEFONT,
                                                     labelanchor='n',
                                                     width=self.objectInfoFrame.winfo_reqwidth() / 2,
                                                     height=self.objectInfoFrame.winfo_reqheight())
        self.individualGenePoolFrame.grid_propagate(False)
        i = 0
        while (i < 7):
            self.individualGenePoolFrame.grid_rowconfigure(i, weight=1)
            i += 1
            self.individualGenePoolFrame.grid_columnconfigure(0, weight=1)
        self.individualGenePoolFrame.grid(column=1, row=0, rowspan=3)
        self.__initIndividualInfoVariables()
        self.individualInfoFrame.grid_remove()
        self.individualGenePoolFrame.grid_remove()


    def __initProgressBarsFrame(self):
        self.loopIndex = 0
        self.currGeneration = 1
        self.loopIndexSpb = tk.IntVar(value=0)
        self.loopIndexScl = tk.IntVar(value=0)
        self.currGenerationSpb = tk.IntVar(value=1)
        self.currGenerationScl = tk.IntVar(value=1)
        self.progressBarsFrame = tk.LabelFrame(self.runInfoFrame,
                            font=H1TITLEFONT,
                            text="Current replay state: ",
                            labelanchor='n',
                            width=self.runInfoFrame.winfo_reqwidth(),
                            height=(self.runInfoFrame.winfo_reqheight() / 12) * 4)
        self.progressBarsFrame.grid_columnconfigure(0, weight=1)
        self.progressBarsFrame.grid_columnconfigure(1, weight=1)
        self.progressBarsFrame.grid_columnconfigure(2, weight=1)
        i = 0
        while (i < 12):
            self.progressBarsFrame.grid_rowconfigure(i, weight=1)
            i += 1
        self.progressBarsFrame.grid_propagate(False)
        self.progressBarsFrame.grid(column=0, columnspan=2, row=2)
        self.__initGenerationsProgressBar()
        self.__initLoopProgressBar()
        self.progressBarsFrame.grid_remove()



    def __initIndividualInfoVariables(self):
        self.lblIndividualPos = tk.Label(self.individualInfoFrame,
                                          font=H3TITLEFONT)
        self.lblIndividualPos.grid(row=0)
        self.lblIndividualHasReproduced = tk.Label(self.individualInfoFrame,
                                          font=H3TITLEFONT)
        self.lblIndividualHasReproduced.grid(row=1)
        self.lblIndividualHasEaten = tk.Label(self.individualInfoFrame,
                                          font=H3TITLEFONT)
        self.lblIndividualHasEaten.grid(row=2)
        self.lblIndividualCurrGoal = tk.Label(self.individualInfoFrame,
                                          font=H3TITLEFONT)
        self.lblIndividualCurrGoal.grid(row=3)
        self.lblIndividualCurrGoalPos = tk.Label(self.individualInfoFrame,
                                          font=H3TITLEFONT)
        self.lblIndividualCurrGoalPos.grid(row=4)
        self.lblIndividualGeneMovement = tk.Label(self.individualGenePoolFrame,
                                              font=H3TITLEFONT)
        self.lblIndividualGeneMovement.grid(row=0)
        self.lblIndividualGeneDanger = tk.Label(self.individualGenePoolFrame,
                                              font=H3TITLEFONT)
        self.lblIndividualGeneDanger.grid(row=1)
        self.lblIndividualGeneFood = tk.Label(self.individualGenePoolFrame,
                                              font=H3TITLEFONT)
        self.lblIndividualGeneFood.grid(row=2)
        self.lblIndividualGeneReproduction = tk.Label(self.individualGenePoolFrame,
                                              font=H3TITLEFONT)
        self.lblIndividualGeneReproduction.grid(row=3)
        self.lblIndividualGeneFertility = tk.Label(self.individualGenePoolFrame,
                                              font=H3TITLEFONT)
        self.lblIndividualGeneFertility.grid(row=4)
        self.lblIndividualGenePreference = tk.Label(self.individualGenePoolFrame,
                                              font=H3TITLEFONT)
        self.lblIndividualGenePreference.grid(row=5)
        self.lblIndividualGeneFear = tk.Label(self.individualGenePoolFrame,
                                              font=H3TITLEFONT)
        self.lblIndividualGeneFear.grid(row=6)


    def __initGenerationsProgressBar(self):
        self.generationBarLblSubFrame = tk.Frame(self.progressBarsFrame,
                                               width=self.progressBarsFrame.winfo_reqwidth() / 2,
                                               height=self.progressBarsFrame.winfo_reqheight() / 6)
        self.generationBarLblSubFrame.grid_columnconfigure(0, weight=1)
        self.generationBarLblSubFrame.grid_columnconfigure(1, weight=1)
        self.generationBarLblSubFrame.grid_columnconfigure(2, weight=1)
        self.generationBarLblSubFrame.grid_rowconfigure(0, weight=1)
        self.generationBarLblSubFrame.grid(column=1, row=2)
        self.lblGenerations = tk.Label(self.generationBarLblSubFrame,
                                        text="Current generation:     ",
                                        font=H3TITLEFONT)
        self.lblGenerations.grid(column=0, row=0)
        self.spbCurrGeneration = tk.Spinbox(self.generationBarLblSubFrame,
                                            from_=1,
                                            to=100,
                                            increment=1,
                                            textvariable=self.currGenerationSpb,
                                            command=self.__changeCurrGenerationSclValue,
                                            font=H4TITLEFONT,
                                            width=3,
                                            justify=tk.RIGHT)
        self.spbCurrGeneration.bind("<Return>", self.__enterChangeSpbCurrGenerationValue)
        self.spbCurrGeneration.grid(column=1, row=0)
        self.lblMaxGeneration = tk.Label(self.generationBarLblSubFrame,
                                          text="/ 100",
                                          font=H3TITLEFONT)
        self.lblMaxGeneration.grid(column=2, row=0)
        self.generationBarProgressSubFrame = tk.Frame(self.progressBarsFrame,
                                              width=self.progressBarsFrame.winfo_reqwidth() / 2,
                                              height=self.progressBarsFrame.winfo_reqheight() / 6)
        self.generationBarProgressSubFrame.grid(column=1, row=3)
        self.sclGenerationBar = tk.Scale(self.generationBarProgressSubFrame,
                                          from_=1,
                                          to=100,
                                          orient=tk.HORIZONTAL,
                                          font=H3TITLEFONT,
                                          variable=self.currGenerationScl,
                                          command=self.__changeCurrGenerationSpbValue,
                                          length=self.progressBarsFrame.winfo_reqwidth()/ 1.5)
        self.sclGenerationBar.grid()

    def __changeCurrGenerationSclValue(self, event=None):
        self.currGenerationScl.set(self.currGenerationSpb.get())
        self.currGeneration = self.currGenerationSpb.get()

    def __changeCurrGenerationSpbValue(self, event=None):
        self.currGenerationSpb.set(self.currGenerationScl.get())
        self.currGeneration = self.currGenerationScl.get()

    def __initLoopProgressBar(self):
        self.loopBarLblSubFrame = tk.Frame(self.progressBarsFrame,
                                               width=self.progressBarsFrame.winfo_reqwidth() / 2,
                                               height=self.progressBarsFrame.winfo_reqheight() / 6)
        self.loopBarLblSubFrame.grid_columnconfigure(0, weight=1)
        self.loopBarLblSubFrame.grid_columnconfigure(1, weight=1)
        self.loopBarLblSubFrame.grid_columnconfigure(2, weight=1)
        self.loopBarLblSubFrame.grid_rowconfigure(0, weight=1)
        self.loopBarLblSubFrame.grid(column=1, row=4)
        self.lblLoops = tk.Label(self.loopBarLblSubFrame,
                                        text="Current loop:     ",
                                        font=H3TITLEFONT)
        self.lblLoops.grid(column=0, row=0)
        self.spbCurrLoop = tk.Spinbox(self.loopBarLblSubFrame,
                                            from_=1,
                                            to=100,
                                            increment=1,
                                            textvariable=self.loopIndexSpb,
                                            command=self.__changeLoopIndexSclValue,
                                            font=H4TITLEFONT,
                                            width=3,
                                            justify=tk.RIGHT)
        self.spbCurrLoop.bind("<Return>", self.__enterChangeSpbCurrLoopValue)
        self.spbCurrLoop.grid(column=1, row=0)
        self.lblMaxLoop = tk.Label(self.loopBarLblSubFrame,
                                          text="/ 100",
                                          font=H3TITLEFONT)
        self.lblMaxLoop.grid(column=2, row=0)
        self.loopBarProgressSubFrame = tk.Frame(self.progressBarsFrame,
                                              width=self.progressBarsFrame.winfo_reqwidth() / 2,
                                              height=self.progressBarsFrame.winfo_reqheight() / 6)
        self.loopBarProgressSubFrame.grid(column=1, row=5)
        self.sclLoopBar = tk.Scale(self.loopBarProgressSubFrame,
                                          from_=1,
                                          to=100,
                                          orient=tk.HORIZONTAL,
                                          variable=self.loopIndexScl,
                                          command=self.__changeLoopIndexSpbValue,
                                          font=H3TITLEFONT,
                                          length=self.progressBarsFrame.winfo_reqwidth()/ 1.5)

        self.sclLoopBar.grid()

    def __enterChangeSpbCurrGenerationValue(self, event=None):
        newValue = int(self.spbCurrGeneration.get())
        self.currGenerationSpb.set(newValue)
        self.currGenerationScl.set(newValue)
        self.currGeneration = newValue

    def __enterChangeSpbCurrLoopValue(self, event=None):
        newValue = int(self.spbCurrLoop.get())
        self.loopIndexSpb.set(newValue)
        self.loopIndexScl.set(newValue)
        self.loopIndex = newValue

    def __changeLoopIndexSclValue(self, event=None):
        self.loopIndexScl.set(self.loopIndexSpb.get())
        self.loopIndex = self.loopIndexSpb.get()

    def __changeLoopIndexSpbValue(self, event=None):
        self.loopIndexSpb.set(self.loopIndexScl.get())
        self.loopIndex = self.loopIndexScl.get()

    def printCurrentlySelectedIndividualInfo(self, individual, menusTab):
        self.placeHolderText.grid_remove()
        self.individualInfoFrame["text"] = "Individual " + individual["name"]
        self.lblIndividualPos["text"] = "Position: [" + str(individual["posX"])\
                                         + ", " + str(individual["posY"]) + "]"
        self.lblIndividualHasEaten["text"] = "Has eaten: " + str(individual["hasEaten"])
        self.lblIndividualHasReproduced["text"] = "Has reproduced: " +\
                                                  str(individual["hasReproduced"])
        self.lblIndividualCurrGoal["text"] = "Current goal: " +\
                                              str(individual["currentGoal"])
        self.lblIndividualCurrGoalPos["text"] = "Goal position: " +\
                                                 str(individual["currentGoalPos"])
        genePool = individual["genePool"]
        self.lblIndividualGeneMovement["text"] = "Movement: " +\
                                                 str(genePool.movement)
        self.lblIndividualGeneDanger["text"] = "Danger radar: " +\
                                                str(genePool.dangerRadar)
        self.lblIndividualGeneFood["text"] = "Food radar: " +\
                                              str(genePool.foodRadar)
        self.lblIndividualGeneReproduction["text"] = "Reproduction radar: " +\
                                                      str(genePool.reproductionRadar)
        self.lblIndividualGeneFertility["text"] = "Fertility: " +\
                                                  str(genePool.fertility)
        self.lblIndividualGenePreference["text"] = "Preference: " +\
                                                    str(genePool.preference)
        self.lblIndividualGeneFear["text"] = "Fear: " + str(genePool.fear)
        self.individualInfoFrame.grid()
        self.individualGenePoolFrame.grid()
        menusTab.select(self.runInfoFrame)

    def setBarsRunValues(self, mainData):
        self.spbCurrGeneration["to"] = mainData.generationsNb
        self.spbCurrGeneration.update()
        self.sclGenerationBar["to"] = mainData.generationsNb
        self.sclGenerationBar.update()
        self.lblMaxGeneration["text"] = "/ " + str(mainData.generationsNb)
        self.lblMaxGeneration.update()
        self.spbCurrLoop["to"] = mainData.generationLifeSpan
        self.spbCurrLoop.update()
        self.sclLoopBar["to"] = mainData.generationLifeSpan
        self.sclLoopBar.update()
        self.lblMaxLoop["text"] = "/ " + str(mainData.generationLifeSpan)

    def correctProgressValues(self, currGeneration, loopIndex):
        self.loopIndexScl.set(loopIndex)
        self.loopIndexSpb.set(loopIndex)
        self.currGenerationScl.set(currGeneration + 1)
        self.currGenerationSpb.set(currGeneration + 1)
        self.loopIndex = loopIndex
        self.currGeneration = currGeneration + 1

    def updatePopulationInfoFrame(self, mainData, loopIndex, currGeneration):
        currInfo = mainData.populationInfoPerLoop[currGeneration][loopIndex]
        self.totalPopulationInfo["text"] = "Total population: " + str(currInfo["popNb"])
        self.populationHasEatenInfo["text"] = "Total that have eaten : "\
                                                + str(currInfo["hasEaten"])
        self.populationHasReproducedInfo["text"] = "Total that have reproduced: "\
                                                    + str(currInfo["hasReproduced"])
