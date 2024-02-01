import pygame
import random
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Set the width and height of each grid cell
WIDTH = 50
HEIGHT = 50


class Screen:
    def __init__(self):
        # Set the size of the screen
        self.size = (WIDTH * 9, HEIGHT * 9)
        # Create a 2D array to represent the Sudoku grid
        self.sudoku_grid = [[0 for _ in range(9)] for _ in range(9)]

    # Create a 2D array to represent the Sudoku grid
    def set_sudoku(self, array):
        self.sudoku_grid = array

    # Function to draw the Sudoku grid
    def draw_grid(self, screen, cages):
        self.draw_cages(screen, cages)
        for i in range(10):
            if i % 3 == 0:
                pygame.draw.line(screen, BLACK, (0, i * HEIGHT), (WIDTH * 9, i * HEIGHT), 2)
                pygame.draw.line(screen, BLACK, (i * WIDTH, 0), (i * WIDTH, HEIGHT * 9), 2)
            else:
                pygame.draw.line(screen, GRAY, (0, i * HEIGHT), (WIDTH * 9, i * HEIGHT))
                pygame.draw.line(screen, GRAY, (i * WIDTH, 0), (i * WIDTH, HEIGHT * 9))

    # Function to draw the numbers in the Sudoku grid
    def draw_numbers(self, screen):
        # Initialize the Pygame font module
        pygame.font.init()
        font = pygame.font.SysFont('BELL.TTF', 36)
        for i in range(9):
            for j in range(9):
                print(i)
                if self.sudoku_grid[i][j] != 0:
                    text = font.render(str(self.sudoku_grid[i][j]), True, BLACK)
                    screen.blit(text, (j * WIDTH + 15, i * HEIGHT + 15))

    # Function to draw cages with borders
    def draw_cages(self, screen, cage_lists):
        # Initialize the Pygame font module
        pygame.font.init()
        font = pygame.font.SysFont('BELL.TTF', 20, italic=True)
        for cage in cage_lists:
            # Convert cell codes to row and column for easier handling
            cells = [((cell // 10) - 1, (cell % 10) - 1) for cell in cage.cells]
            # Find the top-right cell in the cage
            top_right_cell = min(cells, key=lambda x: (x[0], -x[1]))

            for cell in cells:
                row, col = cell
                # Determine borders to draw based on neighboring cells
                borders = []
                if (row - 1, col) not in cells: borders.append('top')
                if (row + 1, col) not in cells: borders.append('bottom')
                if (row, col - 1) not in cells: borders.append('left')  # corrected here
                if (row, col + 1) not in cells: borders.append('right')  # corrected here

                # Calculate the position of the cell
                x = col * WIDTH
                y = row * HEIGHT

                # Draw the border for each necessary side
                for border in borders:
                    if border == 'top':
                        self.draw_dashed_line(screen, cage.color, (x, y), (x + WIDTH, y), 5)
                    elif border == 'bottom':
                        self.draw_dashed_line(screen, cage.color, (x, y + HEIGHT), (x + WIDTH, y + HEIGHT), 5)
                    elif border == 'left':
                        self.draw_dashed_line(screen, cage.color, (x, y), (x, y + HEIGHT), 5)
                    elif border == 'right':
                        self.draw_dashed_line(screen, cage.color, (x + WIDTH, y), (x + WIDTH, y + HEIGHT), 5)

                # If the cell is the top-right cell, draw the cage value
                if (row, col) == top_right_cell:
                    cage_value_text = font.render(str(cage.value), True, cage.color)

                    # Calculate the position to place the value
                    text_x = x + WIDTH - cage_value_text.get_width() - 5  # 5 is a small space from the right edge
                    text_y = y + 5  # 5 is a small space from the top edge

                    # Draw the value on the screen
                    screen.blit(cage_value_text, (text_x, text_y))

    # Function to draw dashed line
    def draw_dashed_line(self, screen, color, start_pos, end_pos, dash_length):
        x1, y1 = start_pos
        x2, y2 = end_pos
        dx = x2 - x1
        dy = y2 - y1
        num_dashes = int(math.hypot(dx, dy) / dash_length)
        for i in range(num_dashes):
            if i % 2 == 0:  # Only draw every second dash
                start = (x1 + i * dx / num_dashes, y1 + i * dy / num_dashes)
                end = (x1 + (i + 1) * dx / num_dashes, y1 + (i + 1) * dy / num_dashes)
                pygame.draw.line(screen, color, start, end, 5)
