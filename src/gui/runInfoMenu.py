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
        self.runInfoFrame.grid_rowconfigure(0, weight=0)
        self.runInfoFrame.grid_rowconfigure(1, weight=0)
        self.__initRunInfoMenuContent()

    def __initRunInfoMenuContent(self):
        self.__initSelectedObjectInfoFrame()

    def __initSelectedObjectInfoFrame(self):
        self.objectInfoFrame = tk.LabelFrame(self.runInfoFrame,
                                          text="Currently selected Object info : ",
                                          labelanchor='n',
                                          font=H1TITLEFONT,
                                          width=self.runInfoFrame.winfo_reqwidth(),
                                          height=self.runInfoFrame.winfo_reqheight() / 3)
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

    def printCurrentlySelectedIndividualInfo(self, individual, menusTab):
        self.placeHolderText.grid_remove()
        self.individualInfoFrame["text"] = "Individual " + individual["name"]
        # self.objectInfoFrame["text"] = "Selected Individual " + individual["name"]
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

