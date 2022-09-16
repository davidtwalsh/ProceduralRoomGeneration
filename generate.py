import generateHallway
from roomTypes import Room
from roomTypes import RoomLayout
from endpoint import Endpoint
from endpoint import EndpointProperties
from perlin import GridPerlinNoise

def generate(NUMROWS, NUMCOLS):

    #create main grid
    grid = [ [0]*NUMCOLS for i in range(NUMROWS)]

    #create perlin noise
    perlinCells = GridPerlinNoise(grid,10,1)

    #Procedural Generation/populate grid
    currentRow = len(grid) // 2
    currentCol = len(grid[0]) // 2

    grid[currentRow][currentCol] = Room.SPAWN #start

    currentCol += 1

    endpoints = []
    e = Endpoint(currentRow,currentCol,Room.HALLWAY,RoomLayout.VERTICAL)
    e.properties.append(EndpointProperties.ISCELLHALLWAY)
    endpoints.append(e) 

    i = 0
    while endpoints:
        endpoint = endpoints.pop(0)
        roomType = endpoint.room
        if roomType == Room.HALLWAY:
                generateHallway.generateHallway(grid,endpoint,endpoints,perlinCells)


        i += 1
    return grid