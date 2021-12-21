import random

class FixedGenePool:
    directions = ["up", "down", "left", "right", "diagUpLeft", "diagUpRight",
                  "diagDownLeft", "diagDownRight"]
    geneLevels = [["movement", 1],
                  ["dangerRadar", 1],
                  ["foodRadar", 1],
                  ["reproductionRadar", 1],
                  ["fertility", 1]]

    def __init__(self, attributesList):
        pass
