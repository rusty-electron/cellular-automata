import numpy as np
import pygame

class Grid():
    def __init__(self, dims = (5, 5), margin = 0, window_size = (800, 800)):
        # set up colours
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)

        # set window and dim values
        self.WINDOW_SIZE = window_size
        self.WIDTH, self.HEIGHT = dims
        self.MARGIN = margin

        # set pixel counts
        self.x_count = self.WINDOW_SIZE[0] // (self.MARGIN + self.WIDTH)
        self.y_count = self.WINDOW_SIZE[1] // (self.MARGIN + self.HEIGHT)

        # create the grid
        self.grid = np.zeros([self.y_count, self.x_count])

    def get_window_size(self):
        return self.WINDOW_SIZE

    def poke(self, pos, val):
        column = pos[0] // (self.WIDTH + self.MARGIN)
        row = pos[1] // (self.HEIGHT + self.MARGIN)
        # Set that location to val
        self.grid[row, column] = val
        return row, column

    def draw_grid(self, screen):
        for row in range(self.y_count):
            for column in range(self.x_count):
                color = self.WHITE
                if self.grid[row, column] == 1:
                    pygame.draw.rect(screen,
                                     color,
                                     [(self.MARGIN + self.WIDTH) * column + self.MARGIN,
                                      (self.MARGIN + self.HEIGHT) * row + self.MARGIN,
                                      self.WIDTH,
                                      self.HEIGHT])

    def set_grid(self, new_grid, screen):
        self.grid = new_grid
        self.draw_grid(screen)

    def get_grid_count(self):
        return (self.y_count, self.x_count)
