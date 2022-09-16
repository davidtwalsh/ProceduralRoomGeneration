import generateHallway
from roomTypes import Room
from roomTypes import RoomLayout
from endpoint import Endpoint
from endpoint import EndpointProperties

def generate(NUMROWS, NUMCOLS):

    grid = [ [0]*NUMCOLS for i in range(NUMROWS)]

    #Procedural Generation/populate grid
    currentRow = len(grid) // 2
    currentCol = len(grid[0]) // 2

    grid[currentRow][currentCol] = Room.SPAWN #start

    currentCol += 1

    endpoints = []
    e = Endpoint(currentRow,currentCol,Room.HALLWAY,RoomLayout.VERTICAL)
    e.properties.append(EndpointProperties.ISCELLHALLWAY)
    endpoints.append(Endpoint(currentRow,currentCol,Room.HALLWAY,RoomLayout.VERTICAL)) 

    i = 0
    while endpoints and i < 1:
        endpoint = endpoints.pop(0)
        roomType = endpoint.room
        if roomType == Room.HALLWAY:
                generateHallway.generateHallway(grid,endpoint,endpoints)


        i += 1
    return grid