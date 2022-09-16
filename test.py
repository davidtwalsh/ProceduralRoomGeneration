import random

def generateHallway(grid,currentRow,currentCol,isVertical):
    
    length = random.randint(3,8)
    isGoingUp = random.choice([True,False])

    if isVertical == True:
        for i in range(length):
            grid[currentRow][currentCol] = 2
            if isGoingUp == True:
                currentRow -= 1
            elif isGoingUp == False:
                currentRow += 1        

    return

grid = [ [0]*10 for i in range(40)]
centerRow = len(grid) // 2
centerCol = len(grid[0]) // 2

grid[centerRow][centerCol] = 1 #start

currentRow = centerRow
currentCol = centerCol + 1

generateHallway(grid,currentRow,currentCol,True)



print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in grid]))