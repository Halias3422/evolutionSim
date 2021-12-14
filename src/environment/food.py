import random


def createMapFreeSpaceListForFood(mapRepresentation, mapSizeX, mapSizeY):
    mapFreeSpaceList = []
    mapSizeY -= 1
    while (mapSizeY >= 0):
        tmpSizeX = mapSizeX - 1
        while (tmpSizeX >= 0):
            if (mapRepresentation[mapSizeY][tmpSizeX] == "empty"):
                freePos = [mapSizeY, tmpSizeX]
                mapFreeSpaceList.append(freePos)
            tmpSizeX -= 1
        mapSizeY -= 1
    return mapFreeSpaceList

def spawnGenerationFood(foodNb, foodVariation, mapSizeX, mapSizeY,
                        mapRepresentation):
    foodQuantity = random.randint(foodNb - foodNb * foodVariation / 100,
                                  foodNb + foodNb * foodVariation / 100)
    foodList = []
    mapFreeSpaceList = createMapFreeSpaceListForFood(mapRepresentation,
                                                     mapSizeX,
                                                     mapSizeY)
    while (foodQuantity > 0):
        initFoodPos = random.choice(mapFreeSpaceList)
        foodPos = [initFoodPos[0], initFoodPos[1]]
        mapFreeSpaceList.remove(foodPos)
        foodList.append(foodPos)
        foodQuantity -= 1
        if (len(mapFreeSpaceList) == 0):
            print("No more space for food")
            break
    return foodList
