import random
from roomTypes import Room
from endpoint import Endpoint
from roomTypes import RoomLayout
from myMath import sign
from myMath import isOutOfBounds
from myMath import isInBounds
from endpoint import EndpointProperties

def generateHallway(grid,endpoint,endpoints):
    
    length = random.randint(10,30)

    currentRow = endpoint.row
    currentCol = endpoint.col

    if endpoint.layout == RoomLayout.VERTICAL:
        changeFactor = 0
        for i in range(length):
            if changeFactor < 0:
                changeFactor = i
            else:
                changeFactor = i * -1
            currentRow += changeFactor

            if isOutOfBounds(currentRow,currentCol,grid):
                return

            if grid[currentRow][currentCol] != 0:
                return

            grid[currentRow][currentCol] = Room.HALLWAY

            if EndpointProperties.ISCELLHALLWAY in endpoint.properties:
                
                if abs(i) % 2 == 0:
                    if isInBounds(currentRow,currentCol-1,grid) and grid[currentRow][currentCol-1] == 0:
                        print("made cell")
                        grid[currentRow][currentCol-1] = Room.CELL
                    if isInBounds(currentRow,currentCol+1,grid) and grid[currentRow][currentCol+1] == 0:
                        print("made cell 2")
                        grid[currentRow][currentCol+1] = Room.CELL


            if length - i <= 2:
                e = Endpoint(currentRow + 1 * sign(changeFactor),currentCol,Room.HALLWAY,RoomLayout.HORIZONTAL)
                endpoints.append(e)
                randomForCell = random.randint(1,10)
                if randomForCell <= 2:
                    e.properties.append(EndpointProperties.ISCELLHALLWAY)

    elif endpoint.layout == RoomLayout.HORIZONTAL:
        changeFactor = 0
        for i in range(length):
            if changeFactor < 0:
                changeFactor = i
            else:
                changeFactor = i * -1
            currentCol += changeFactor

            if isOutOfBounds(currentRow,currentCol,grid):
                return

            if grid[currentRow][currentCol] != 0:
                return
            grid[currentRow][currentCol] = Room.HALLWAY

            if EndpointProperties.ISCELLHALLWAY in endpoint.properties:
                if abs(i) % 2 == 0:
                    if isInBounds(currentRow+1,currentCol,grid) and grid[currentRow+1][currentCol] == 0:
                        grid[currentRow+1][currentCol] = Room.CELL
                    if isInBounds(currentRow-1,currentCol,grid) and grid[currentRow-1][currentCol] == 0:
                        grid[currentRow-1][currentCol] = Room.CELL

            if length - i <= 2:
                e = Endpoint(currentRow,currentCol + 1 * sign(changeFactor),Room.HALLWAY,RoomLayout.VERTICAL)
                endpoints.append(e)
                randomForCell = random.randint(1,10)
                if randomForCell <= 2:
                    e.properties.append(EndpointProperties.ISCELLHALLWAY)
                 

    return