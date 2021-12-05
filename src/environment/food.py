import random


def spawnGenerationFood(foodNb, foodVariation, mapSizeX, mapSizeY,
                        mapRepresentation):
    foodQuantity = random.randint(foodNb - foodNb * foodVariation / 100,
                                  foodNb + foodNb * foodVariation / 100)
    foodList = []
    while (foodQuantity > 0):
        while True:
            foodPos = [random.randint(0, mapSizeY - 1),
                       random.randint(0, mapSizeX - 1)]
            if ((foodPos not in foodList)
                    and (mapRepresentation[foodPos[0]][foodPos[1]] == 0)):
                foodList.append(foodPos)
                foodQuantity -= 1
                break
    return foodList
