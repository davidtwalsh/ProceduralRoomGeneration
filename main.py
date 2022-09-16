from tkinter.tix import CELL
import pygame
import generate
import colors
from roomTypes import RoomColors
from roomTypes import Room
import colors

WIDTH = 1600
HEIGHT = 1000
FPS = 30


## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("<Your game>")
clock = pygame.time.Clock()     ## For syncing the FPS

#for cell generation
CELLWIDTH = 10
NUMROWS = HEIGHT // CELLWIDTH
NUMCOLS = WIDTH // CELLWIDTH

grid = generate.generate(NUMROWS,NUMCOLS)

## Game loop
running = True
while running:

    #1 Process input/events
    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                grid = generate.generate(NUMROWS,NUMCOLS)

    ########################

    ### updating


    ########################

    #3 Draw/render
    screen.fill(colors.BLACK)

    ########################

    ### drawing

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                pygame.draw.rect(screen, colors.BLACK, pygame.Rect(col * CELLWIDTH, row * CELLWIDTH, CELLWIDTH, CELLWIDTH))
            elif grid[row][col] == Room.SPAWN:
                pygame.draw.rect(screen, RoomColors.roomColors[Room.SPAWN], pygame.Rect(col * CELLWIDTH, row * CELLWIDTH, CELLWIDTH, CELLWIDTH))
            elif grid[row][col] == Room.HALLWAY:
                pygame.draw.rect(screen, RoomColors.roomColors[Room.HALLWAY], pygame.Rect(col * CELLWIDTH, row * CELLWIDTH, CELLWIDTH, CELLWIDTH))
            elif grid[row][col] == Room.CELL:
                pygame.draw.rect(screen, RoomColors.roomColors[Room.HALLWAY], pygame.Rect(col * CELLWIDTH, row * CELLWIDTH, CELLWIDTH, CELLWIDTH))
            

    ########################

    ## Done after drawing everything to the screen
    pygame.display.flip()       

pygame.quit()