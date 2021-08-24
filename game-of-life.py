import pygame
import numpy as np
from common import Grid

class GoL():
    def __init__(self, grid_size):
        # create an empty grid
        self.life_grid = np.zeros(grid_size)
        self.grid_size = grid_size

    def neighbour_sum(self, pos):
        row, col = pos

        row = row + 1
        col = col + 1
        sum_val = self.padded_grid[row - 1:row + 2, col - 1:col + 2].sum()
        if self.padded_grid[row, col]:
            return sum_val - 1
        else:
            return sum_val

    def refresh_padded_grid(self):
        self.padded_grid = np.pad(self.life_grid, 1, mode='constant')

    def set_grid(self, grid_arr):
        self.life_grid = grid_arr

    def get_grid(self):
        return self.life_grid

    def alive(self, pos):
        return self.life_grid[pos[0], pos[1]] > 0

    def kill(self, pos):
        self.life_grid[pos[0], pos[1]] = 0

    def revive(self, pos):
        self.life_grid[pos[0], pos[1]] = 1

    def process(self):
        self.refresh_padded_grid()
        row_count, col_count = self.grid_size
        for row in range(row_count):
            for col in range(col_count):
                pos = (row, col)
                if self.alive(pos):
                    if self.neighbour_sum(pos) == 2 or self.neighbour_sum(pos) == 3:
                        self.revive(pos)
                    else:
                        self.kill(pos)
                else:
                    if self.neighbour_sum(pos) == 3:
                        self.revive(pos)

if __name__ == "__main__":
    pygame.init()
    mygrid = Grid(dims=(8, 8), margin=0)

    # instead of the poke method, one can use do this manually
    # mygrid.grid[1][5] = 1

    screen = pygame.display.set_mode(mygrid.get_window_size())
    pygame.display.set_caption("Game of Life")

    done = False
    # used to manage how fast the screen updates
    clock = pygame.time.Clock()

    init_gol = GoL(mygrid.get_grid_count())
    rand_grid = (np.random.random(mygrid.get_grid_count()) > 0.5).astype(np.int32)

    init_gol.set_grid(rand_grid)

    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                row, column = mygrid.poke(pos, 1)
                print("Click ", pos, "Grid coordinates: ", row, column)

        # just a test
        # set the screen background
        screen.fill(mygrid.BLACK)

        init_gol.process()
        mygrid.set_grid(init_gol.get_grid(), screen)
        pygame.time.wait(200)
        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    pygame.quit()
