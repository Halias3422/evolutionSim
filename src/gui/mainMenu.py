import tkinter as tk

H1TITLEFONT = ("Arial", 20)
H2TITLEFONT = ("Arial", 18)
H3TITLEFONT = ("Arial", 16)
H4TITLEFONT = ("Arial", 14)
DEFAULTPOPSIZE = 10
DEFAULTFOODNB = 10
DEFAULTMAPSIZE=5
DEFAULTGENLIFE=100
DEFAULTGENNB=2
DEFAULTDANGERNB=0
DEFAULTOBSTACLENB=0
DEFAULTMUTATION=100

class MainMenu:

    def __init__(self, menusTabs, mainWindow, frameLength, frameHeight,
                 runGenerationsLife, applicationGUI):
        self.__createNewLifeCycleFrame(frameLength, frameHeight, menusTabs)
        mainWindow.update_idletasks()
        self.__initMenusContent(runGenerationsLife, applicationGUI)
        mainWindow.update_idletasks()


    def __initMenusContent(self, runGenerationsLife, applicationGUI):
        self.__initMainMenuRunDataFrameContent()
        self.__initMainMenuOptionsFrameContent(applicationGUI)
        self.__createRunButton(runGenerationsLife, applicationGUI)
        self.__createLoadingInfosDisplay()

    def __createLoadingInfosDisplay(self):
        self.loadingInfoFrame = tk.LabelFrame(self.menusFrame,
                                              text="Currently creating life...",
                                              font=H3TITLEFONT,
                                              labelanchor='n',
                                              width=self.menusFrame.winfo_reqwidth(),
                                              height=self.menusFrame.winfo_reqheight() / 5)
        self.loadingInfoFrame.pack_propagate(False)
        self.loadingInfoFrame.grid(column=0, columnspan=2, row=2)

        self.lblCurrentGeneration = tk.Label(self.loadingInfoFrame,
                                             text="",
                                             font=H4TITLEFONT)
        self.lblCurrentGeneration.pack()
        self.lblLoadingPopulationSize = tk.Label(self.loadingInfoFrame,
                                                 text="",
                                                 font=H4TITLEFONT)
        self.lblLoadingPopulationSize.pack()
        self.lblLoadingHasReproduced = tk.Label(self.loadingInfoFrame,
                                                text="",
                                                font=H4TITLEFONT)
        self.lblLoadingHasReproduced.pack()
        self.lblLoadingHasEaten = tk.Label(self.loadingInfoFrame,
                                                text="",
                                                font=H4TITLEFONT)
        self.lblLoadingHasEaten.pack()
        self.lblLoadingHasReproducedAndEaten = tk.Label(self.loadingInfoFrame,
                                                text="",
                                                font=H4TITLEFONT)
        self.lblLoadingHasReproducedAndEaten.pack()

        self.loadingInfoFrame.grid_remove()



    def __initMainMenuOptionsFrameContent(self, applicationGUI):
        self.optionsFrame = tk.LabelFrame(self.menusFrame,
                                    text="Options : ",
                                    font=H2TITLEFONT,
                                    labelanchor="n",
                                    width=self.menusFrame.winfo_reqwidth() / 2,
                                    height=int((self.menusFrame.winfo_reqheight() / 3) * 2))
        self.optionsFrame.grid_propagate(False)
        self.optionsFrame.grid_columnconfigure(0, weight=1)
        self.optionsFrame.grid_rowconfigure(0, weight=1)
        self.optionsFrame.grid_rowconfigure(1, weight=1)
        self.optionsFrame.grid_rowconfigure(2, weight=1)
        self.optionsFrame.grid_rowconfigure(3, weight=1)
        self.optionsFrame.grid_rowconfigure(4, weight=1)
        self.optionsFrame.grid(column=1, row=0, sticky='N')
        self.__createOptionsFrameContent(applicationGUI)

    def __createRunButton(self, runGenerationsLife, applicationGUI):
        self.runButton = tk.Button(self.menusFrame, text="\n    CREATE LIFE    \n",
                              font=("Arial", 32), bg="green", fg="white",
                              command=lambda: runGenerationsLife(applicationGUI))
        self.runButton.bind("<Return>", lambda event,:  runGenerationsLife(applicationGUI))
        self.runButton.grid(column=0, columnspan=2, row=1, pady=20)
        self.runButton.focus_set()

    def __initMainMenuRunDataFrameContent(self):
        self.runDataFrame = tk.LabelFrame(self.menusFrame,
                                     text="Run Datas : ",
                                     font=H2TITLEFONT,
                                     labelanchor="n",
                                     width=self.menusFrame.winfo_reqwidth() / 2,
                                     height=int((self.menusFrame.winfo_reqheight() / 3) * 2))
        self.runDataFrame.pack_propagate(False)
        self.runDataFrame.grid(column=0, row=0, sticky='N')
        self.__createRunDataFrameContent()

    def __createOptionsFrameContent(self, applicationGUI):
        self.populationGenFrame = self.__createOptionsSubFrames(" Population generation: ", 0, 4)
        self.dangerGenFrame = self.__createOptionsSubFrames(" Danger zones generation: ", 1, 4)
        self.foodGenFrame = self.__createOptionsSubFrames(" Food generation: ", 2, 5)
        self.obstacleGenFrame = self.__createOptionsSubFrames(" Obstacles generation: ", 3, 4)
        self.reproductionGenFrame = self.__createOptionsSubFrames(" Reproduction toggle: ", 4, 3)
        self.__createOptionsPopulationNumber()
        self.__createOptionsDangerGeneration()
        self.__createOptionsFoodGeneration()
        self.__createOptionsObstacleGeneration()
        self.__createOptionsReproductionGeneration()

    def __createOptionsSubFrames(self, frameText, frameRowPlace, frameColumnNb):
        optionSubFrame = tk.LabelFrame(self.optionsFrame,
                                       font=H3TITLEFONT,
                                       text=frameText,
                                       labelanchor='n',
                                       width=self.optionsFrame.winfo_reqwidth(),
                                       height=self.optionsFrame.winfo_reqheight() / 5)
        optionSubFrame.grid_propagate(False)
        optionSubFrame.grid_rowconfigure(0, weight=1)
        currColumn = 0
        while (currColumn < frameColumnNb):
            optionSubFrame.grid_columnconfigure(currColumn, weight=1)
            currColumn += 1
        optionSubFrame.grid(column=0, row=frameRowPlace)
        return optionSubFrame

    def __createOptionsReproductionGeneration(self):
        self.optionReproductionGen = tk.BooleanVar(value=False)
        self.cbxOptionDisableReproduction = tk.Checkbutton(self.reproductionGenFrame,
                                                           text="Disable",
                                                           variable=self.optionReproductionGen,
                                                           font=H4TITLEFONT)
        self.cbxOptionDisableReproduction.grid(column=1, row=0)

    def __createOptionsObstacleGeneration(self):
        self.optionObstacleGen = tk.StringVar(value="random")
        self.rdbOptionPaintObstacle = self.__addPaintRadioButton(self.obstacleGenFrame,
                                                              self.optionObstacleGen)
        self.rdbOptionPaintObstacle["command"] = self.__disableObstacleTxt
        self.rdbOptionRandomObstacle = self.__addRandomRadioButton(self.obstacleGenFrame,
                                                               self.optionObstacleGen)
        self.rdbOptionRandomObstacle["command"] = self.__enableObstacleTxt

    def __enableObstacleTxt(self):
        self.txtObstacleNb["state"] = tk.NORMAL

    def __disableObstacleTxt(self):
        self.txtObstacleNb["state"] = tk.DISABLED

    def __createOptionsFoodGeneration(self):
        self.optionFoodGen = tk.StringVar(value="random")
        self.rdbOptionPaintFood = self.__addPaintRadioButton(self.foodGenFrame,
                                                              self.optionFoodGen)
        self.rdbOptionPaintFood["command"] = self.__disableTxtFoodNb
        self.rdbOptionRandomFood = self.__addRandomRadioButton(self.foodGenFrame,
                                                               self.optionFoodGen)
        self.rdbOptionRandomFood["command"] = self.__enableTxtFoodNb
        self.rdbOptionDisableFood = tk.Radiobutton(self.foodGenFrame,
                                                   text="Disable",
                                                   value="disable",
                                                   variable=self.optionFoodGen,
                                                   command=self.__disableTxtFoodNb,
                                                   font=H4TITLEFONT)
        self.rdbOptionDisableFood.grid(column=3, row=0)

    def __enableTxtFoodNb(self):
        self.txtFoodNb["state"] = tk.NORMAL

    def __disableTxtFoodNb(self):
        self.txtFoodNb["state"] = tk.DISABLED

    def __addRandomRadioButton(self, motherFrame, motherVariable):
        rdbRandomOption = tk.Radiobutton(motherFrame,
                                        text="Random",
                                        value="random",
                                        variable=motherVariable,
                                        font=H4TITLEFONT)
        rdbRandomOption.grid(column=2, row=0)
        return rdbRandomOption

    def __addPaintRadioButton(self, motherFrame, motherVariable):
        rdbPaintOption = tk.Radiobutton(motherFrame,
                                             text="Paint",
                                             value="paint",
                                             variable=motherVariable,
                                             font=H4TITLEFONT)
        rdbPaintOption.grid(column=1, row=0)
        return rdbPaintOption

    def __createOptionsDangerGeneration(self):
        self.optionDangerGen = tk.StringVar(value="random")
        self.rdbOptionPaintDanger = self.__addPaintRadioButton(self.dangerGenFrame,
                                                               self.optionDangerGen)
        self.rdbOptionPaintDanger["command"] = self.__disableDangerNbInput
        self.rdbOptionRandomDanger = self.__addRandomRadioButton(self.dangerGenFrame,
                                                                 self.optionDangerGen)
        self.rdbOptionRandomDanger["command"] = self.__enableDangerNbInput
        self.rdbOptionRandomDanger.select()

    def __enableDangerNbInput(self):
        self.txtDangerNb["state"] = tk.NORMAL

    def __disableDangerNbInput(self):
        self.txtDangerNb["state"] = tk.DISABLED

    def __createOptionsPopulationNumber(self):
        self.optionPopulationGen = tk.StringVar(value="fixed")
        self.rdbOptionFixedPopulationNb = tk.Radiobutton(self.populationGenFrame,
                                                 text="Fixed",
                                                 value="fixed",
                                                 variable=self.optionPopulationGen,
                                                 font=H4TITLEFONT)
        self.rdbOptionFixedPopulationNb.grid(column=1, row=0, sticky='w')

        self.rdbOptionChildrenPopulationNb = tk.Radiobutton(self.populationGenFrame,
                                                text="Survivors Children",
                                                value="children",
                                                variable=self.optionPopulationGen,
                                                font=H4TITLEFONT)
        self.rdbOptionChildrenPopulationNb.grid(column=2, row=0, sticky='w')
        self.rdbOptionFixedPopulationNb.select()

    def __createRunDataFrameContent(self):
        lblPopulationSize = tk.Label(self.runDataFrame,
                                     font=H3TITLEFONT,
                                     text="Population Size: ")
        lblPopulationSize.pack()
        self.txtPopulationSize = tk.Entry(self.runDataFrame, font=H3TITLEFONT)
        self.txtPopulationSize.insert(0, str(DEFAULTPOPSIZE))
        self.txtPopulationSize.pack()

        lblFoodNb = tk.Label(self.runDataFrame,
                             font=H3TITLEFONT,
                             text="Food Units Available : ")
        lblFoodNb.pack()
        self.txtFoodNb = tk.Entry(self.runDataFrame, font=H3TITLEFONT)
        self.txtFoodNb.insert(0, str(DEFAULTFOODNB))
        self.txtFoodNb.pack()

        lblMapSize = tk.Label(self.runDataFrame, font=H3TITLEFONT,
                              text="Map Size (X and Y): ")
        lblMapSize.pack()
        self.txtMapSize = tk.Entry(self.runDataFrame, font=H3TITLEFONT)
        self.txtMapSize.insert(0, str(DEFAULTMAPSIZE))
        self.txtMapSize.pack()

        lblGenerationLifeSpan = tk.Label(self.runDataFrame, font=H3TITLEFONT,
                                         text="Generation Life Span : ")
        lblGenerationLifeSpan.pack()
        self.txtGenerationLifeSpan = tk.Entry(self.runDataFrame, font=H3TITLEFONT)
        self.txtGenerationLifeSpan.insert(0, str(DEFAULTGENLIFE))
        self.txtGenerationLifeSpan.pack()

        lblGenerationNb = tk.Label(self.runDataFrame, font=H3TITLEFONT,
                                   text="Generations Number : ")
        lblGenerationNb.pack()
        self.txtGenerationNb = tk.Entry(self.runDataFrame, font=H3TITLEFONT)
        self.txtGenerationNb.insert(0, str(DEFAULTGENNB))
        self.txtGenerationNb.pack()

        lblDangerNb = tk.Label(self.runDataFrame, font=H3TITLEFONT,
                               text="Danger Zones Tiles : ")
        lblDangerNb.pack()
        self.txtDangerNb = tk.Entry(self.runDataFrame, font=H3TITLEFONT)
        self.txtDangerNb.insert(0, str(DEFAULTDANGERNB))
        self.txtDangerNb.pack()

        lblObstacleNb = tk.Label(self.runDataFrame, font=H3TITLEFONT,
                                 text="Obstacles Tiles : ")
        lblObstacleNb.pack()
        self.txtObstacleNb = tk.Entry(self.runDataFrame, font=H3TITLEFONT)
        self.txtObstacleNb.insert(0, str(DEFAULTOBSTACLENB))
        self.txtObstacleNb.pack()

        lblMutationProb = tk.Label(self.runDataFrame, font=H3TITLEFONT,
                                    text="Mutation Probability (%) : ")
        lblMutationProb.pack()
        self.txtMutationProb = tk.Entry(self.runDataFrame, font=H3TITLEFONT)
        self.txtMutationProb.insert(0, str(DEFAULTMUTATION))
        self.txtMutationProb.pack()

    def __createNewLifeCycleFrame(self, frameLength, frameHeight, menusTabs):
        self.menusFrame = tk.LabelFrame(menusTabs,
                                   text="Create new Life Cycle : ",
                                   font=H1TITLEFONT,
                                   labelanchor="n",
                                   width=frameLength,
                                   height=frameHeight)
        self.menusFrame.grid_propagate(False)
        self.menusFrame.pack()
        self.menusFrame.grid_columnconfigure(0, weight=1)
        self.menusFrame.grid_columnconfigure(1, weight=1)
        self.menusFrame.grid_rowconfigure(0, weight=0)
        self.menusFrame.grid_rowconfigure(1, weight=0)
        self.menusFrame.grid_rowconfigure(2, weight=0)

    def printLoadingInit(self, mainWindow):
        self.lblCurrentGeneration["text"] = "Initializing life creation..."
        self.loadingInfoFrame.grid()
        mainWindow.update()

    def printCurrentLoadingDatas(self, dataCollection, currentLoop, mainWindow,
                                 generationsNb):
        if (dataCollection is None or currentLoop  + 1 >= generationsNb):
            self.loadingInfoFrame.grid_remove()
            return
        self.lblCurrentGeneration["text"] = ("Generation "
                                             + str(currentLoop + 1) + "/"
                                             + str(generationsNb) + " done")
        self.lblLoadingPopulationSize["text"] = ("Initial population size : "
                                                + str(dataCollection.populationSize))
        self.lblLoadingHasReproduced["text"] = ("Individuals that have reproduced : "
                                                + str(dataCollection.hasReproducedNb))
        self.lblLoadingHasEaten["text"] = ("Individuals that have eaten : "
                                            + str(dataCollection.hasEatenNb))
        self.lblLoadingHasReproducedAndEaten["text"] = ("Individual that have reproduced and eaten : "
                                                         + str(dataCollection.hasReproducedAndEatenNb))
        self.loadingInfoFrame.grid()
        mainWindow.update()




