
def sign(x):
    if x >= 0:
        return 1
    else:
        return -1

def isOutOfBounds(row,col,grid):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return True
    else:
        return False

def isInBounds(row,col,grid):
    return not isOutOfBounds(row,col,grid)