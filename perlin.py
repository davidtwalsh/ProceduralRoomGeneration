from perlin_noise import PerlinNoise

#Each pixel in self.pic will return a value between 0 and 1 correspending to map grid
class GridPerlinNoise:
    def __init__(self,grid,_octaves,_seed):
        noise = PerlinNoise(octaves=_octaves, seed=_seed)
        xpix, ypix = len(grid[0]), len(grid)
        self.pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

        for row in range(len(self.pic)):
            for col in range(len(self.pic[0])):
                pixel = self.pic[row][col]
                pixel += .5

    def getNoiseAtCoordinates(self,row,col):
        return self.pic[row][col]