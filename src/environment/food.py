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

def getFoodListFromMapRepresentation(mainData):
    foodList = []
    currY = mainData.mapSizeY - 1

    while (currY >= 0):
        currX = mainData.mapSizeX - 1
        while (currX >= 0):
            if (mainData.mapRepresentation[currY][currX] == "food"):
                foodList.append([currY, currX])
            currX -= 1
        currY -= 1
    return foodList

def spawnGenerationFood(foodNb, mapSizeX, mapSizeY,
                        mapRepresentation):
    foodQuantity = random.randint(foodNb - foodNb , foodNb + foodNb)
    foodList = []
    mapFreeSpaceList = createMapFreeSpaceListForFood(mapRepresentation,
                                                     mapSizeX,
                                                     mapSizeY)
    while (foodQuantity > 0):
        if (len(mapFreeSpaceList) > 0):
            initFoodPos = random.choice(mapFreeSpaceList)
            foodPos = [initFoodPos[0], initFoodPos[1]]
            mapFreeSpaceList.remove(foodPos)
            foodList.append(foodPos)
            foodQuantity -= 1
        else:
            print("No more space for food")
            return foodList
    return foodList
