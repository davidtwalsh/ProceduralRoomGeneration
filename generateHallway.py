import random
from roomTypes import Room
from endpoint import Endpoint
from roomTypes import RoomLayout
from myMath import sign
from myMath import isOutOfBounds
from myMath import isInBounds
from endpoint import EndpointProperties

def generateOneDirection(grid, endpoint,endpoints,length, isVertical):

    currentRow = endpoint.row
    currentCol = endpoint.col

    skips = 0
    changeFactor = 0
    for i in range(length):
        if changeFactor < 0:
            changeFactor = i
        else:
            changeFactor = i * -1

        if isVertical == True:
            currentRow += changeFactor
        else:
            currentCol += changeFactor

        if isOutOfBounds(currentRow,currentCol,grid):
            return

        if grid[currentRow][currentCol] != 0:
            return

        grid[currentRow][currentCol] = Room.HALLWAY

        if EndpointProperties.ISCELLHALLWAY in endpoint.properties:
            if (isVertical):
                if i == 0 or (changeFactor > 0 and i % 4 == 0) or (changeFactor < 0 and (i+1) % 4 == 0):
                    if isInBounds(currentRow,currentCol-1,grid) and grid[currentRow][currentCol-1] == 0:
                        grid[currentRow][currentCol-1] = Room.CELL
                    if isInBounds(currentRow,currentCol+1,grid) and grid[currentRow][currentCol+1] == 0:
                        grid[currentRow][currentCol+1] = Room.CELL
            else:
                if abs(i) % 2 == 0:
                    if isInBounds(currentRow+1,currentCol,grid) and grid[currentRow+1][currentCol] == 0:
                        grid[currentRow+1][currentCol] = Room.CELL
                    if isInBounds(currentRow-1,currentCol,grid) and grid[currentRow-1][currentCol] == 0:
                        grid[currentRow-1][currentCol] = Room.CELL


        if length - i <= 2:
            e = None
            if isVertical:
                e = Endpoint(currentRow + 1 * sign(changeFactor),currentCol,Room.HALLWAY,RoomLayout.HORIZONTAL)
            else:
                e = Endpoint(currentRow,currentCol+ 1 * sign(changeFactor),Room.HALLWAY,RoomLayout.VERTICAL)
            endpoints.append(e)
            randomForCell = random.randint(1,10)
            if randomForCell <= 2:
                e.properties.append(EndpointProperties.ISCELLHALLWAY)

def generateHallway(grid,endpoint,endpoints):
    
    length = random.randint(10,30)

    if endpoint.layout == RoomLayout.VERTICAL:
        generateOneDirection(grid,endpoint,endpoints,length,True)
    elif endpoint.layout == RoomLayout.HORIZONTAL:
        generateOneDirection(grid,endpoint,endpoints,length,False)
                 

    return