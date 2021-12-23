import tkinter as tk
from tkinter import ttk
from .dangerPaintingMode import enterDangerPaintingMode

H1TITLEFONT = ("Arial", 20)
H2TITLEFONT = ("Arial", 18)
H3TITLEFONT = ("Arial", 16)
H4TITLEFONT = ("Arial", 14)
DEFAULTPOPSIZE = 10
DEFAULTFOODNB = 10
DEFAULTFOODVARIATION = 0
DEFAULTMAPSIZE=5
DEFAULTGENLIFE=100
DEFAULTGENNB=2
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
                                    height=self.menusFrame.winfo_reqheight() / 2)
        self.optionsFrame.pack_propagate(False)
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
                                     height=self.menusFrame.winfo_reqheight() / 2)
        self.runDataFrame.pack_propagate(False)
        self.runDataFrame.grid(column=0, row=0, sticky='N')
        self.__createRunDataFrameContent()

    def __createOptionsFrameContent(self, applicationGUI):
        self.__createOptionsFramePopulationGen()
        self.__createOptionsFrameToggles()
        self.__createPaintDangerButton(applicationGUI)

    def __createPaintDangerButton(self, applicationGUI):
        self.paintDangerButton = tk.Button(self.optionsFrame,
                                           font=H3TITLEFONT,
                                           text="Paint danger zones",
                                           bg="grey",
                                           fg="white",
                                           command=lambda: enterDangerPaintingMode(applicationGUI))
        self.paintDangerButton.pack(pady=10)


    def __createOptionsFrameToggles(self):
        self.optionsToggles = tk.LabelFrame(self.optionsFrame,
                                            font=H3TITLEFONT,
                                            text="Toggle ON/OFF",
                                            labelanchor="n",
                                            width=self.menusFrame.winfo_reqwidth() / 2,
                                            height=self.menusFrame.winfo_reqheight() / 6)
        self.optionsToggles.pack_propagate(False)
        self.optionsToggles.pack(pady=10)

        self.dangerToggle = tk.IntVar()
        self.cbxDangerToggle = tk.Checkbutton(self.optionsToggles,
                                           font=H4TITLEFONT,
                                           text="Danger",
                                           variable=self.dangerToggle)
        self.cbxDangerToggle.pack(anchor=tk.W)
        self.cbxDangerToggle.select()

        self.foodToggle = tk.IntVar()
        self.cbxFoodToggle = tk.Checkbutton(self.optionsToggles,
                                            font=H4TITLEFONT,
                                            text="Food",
                                            variable=self.foodToggle)
        self.cbxFoodToggle.pack(anchor=tk.W)
        self.cbxFoodToggle.select()

        self.reproductionToggle = tk.IntVar()
        self.cbxReproductionToggle = tk.Checkbutton(self.optionsToggles,
                                            font=H4TITLEFONT,
                                            text="Reproduction",
                                            variable=self.reproductionToggle)
        self.cbxReproductionToggle.pack(anchor=tk.W)
        self.cbxReproductionToggle.select()

        self.mutationToggle = tk.IntVar()
        self.cbxMutationToggle = tk.Checkbutton(self.optionsToggles,
                                            font=H4TITLEFONT,
                                            text="mutation",
                                            variable=self.mutationToggle)
        self.cbxMutationToggle.pack(anchor=tk.W)
        self.cbxMutationToggle.select()

    def __createOptionsFramePopulationGen(self):
        self.optionPopulationGen = tk.StringVar(value="fixed")
        self.populationGenFrame = tk.LabelFrame(self.optionsFrame,
                                            font=H3TITLEFONT,
                                            text="Population number each Generation : ",
                                            labelanchor="n",
                                            width=self.menusFrame.winfo_reqwidth() / 2,
                                            height=self.menusFrame.winfo_reqheight() / 10)
        self.populationGenFrame.pack_propagate(False)
        self.populationGenFrame.pack(pady=10)

        self.rdbOptionFixedPopulationNb = tk.Radiobutton(self.populationGenFrame,
                                                 text="Fixed",
                                                 value="fixed",
                                                 variable=self.optionPopulationGen,
                                                 font=H4TITLEFONT)
        self.rdbOptionFixedPopulationNb.pack(anchor=tk.W)

        self.rdbOptionChildrenPopulationNb = tk.Radiobutton(self.populationGenFrame,
                                                text="Survivors Children",
                                                value="children",
                                                variable=self.optionPopulationGen,
                                                font=H4TITLEFONT)
        self.rdbOptionChildrenPopulationNb.pack(anchor=tk.W)
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

        lblFoodVariation = tk.Label(self.runDataFrame,
                                    font=H3TITLEFONT,
                                    text="Food Variation (%) : ")
        lblFoodVariation.pack()
        self.txtFoodVariation = tk.Entry(self.runDataFrame, font=H3TITLEFONT)
        self.txtFoodVariation.insert(0, str(DEFAULTFOODVARIATION))
        self.txtFoodVariation.pack()

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




