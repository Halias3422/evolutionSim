import random


class Individual:

    def __init__(self, mapSizeX, mapSizeY):
        # self.posX = random.randint(0, mapSizeX - 1)
        # self.posY = random.randint(0, mapSizeY - 1)
        self.mapPosition = [random.randint(0, mapSizeX - 1),
                            random.randint(0, mapSizeY - 1)]
