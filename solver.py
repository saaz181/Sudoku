import copy

from screen import *


def solve(Scr: Screen, show):
    for row in range(9):
        for col in range(9):
            if Scr.sudoku_grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(num, row, col, Scr):
                        Scr.sudoku_grid[row][col] = num  # Make the change
                        if forward_check(Scr, row, col) and solve(Scr, show):
                            return True  # If successful, propagate the success back up
                        Scr.sudoku_grid[row][col] = 0  # Revert the change on failure
                        Scr.draw_grid(show)
                return False  # If no number is valid, backtrack
    return True  # If the end of the grid is reached, the puzzle is solved


def forward_check(Scr: Screen, row, col):
    # Check if there is at least one valid number for each empty cell in the same row, column, and box
    for i in range(9):
        if i != col and Scr.sudoku_grid[row][i] == 0 and not any(is_valid(num, row, i, Scr) for num in range(1, 10)):
            return False
        if i != row and Scr.sudoku_grid[i][col] == 0 and not any(is_valid(num, i, col, Scr) for num in range(1, 10)):
            return False

    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if (i + start_row != row or j + start_col != col) and Scr.sudoku_grid[i + start_row][j + start_col] == 0:
                if not any(is_valid(num, i + start_row, j + start_col, Scr) for num in range(1, 10)):
                    return False

    return True


def is_valid(num, row, col, Scr: Screen):
    # Check the number in the current row
    if num in Scr.sudoku_grid[row]:
        return False

    # Check the number in the current column
    if num in [Scr.sudoku_grid[i][col] for i in range(9)]:
        return False

    # Check the number in the current box
    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if Scr.sudoku_grid[i + start_row][j + start_col] == num:
                return False

    # Check the number in the current cage
    for cage in Scr.cages:
        cells = [(cell // 10 - 1, cell % 10 - 1) for cell in cage.cells]
        if (row, col) in cells:
            # Check if the number is already in this cage
            for cell in cells:
                r, c = cell
                if Scr.sudoku_grid[r][c] == num:
                    return False

            current_sum = num  # Start with the number we're trying to place
            for cell in cells:
                r, c = cell
                if Scr.sudoku_grid[r][c] != 0:
                    current_sum += Scr.sudoku_grid[r][c]
            # Check if the sum exceeds the cage's value
            if current_sum > cage.value:
                return False
            # Check if this is the last cell to fill in the cage and the sum doesn't match the cage's value
            empty_cells = sum(1 for cell in cells if Scr.sudoku_grid[cell[0]][cell[1]] == 0)
            if empty_cells == 1 and current_sum != cage.value:
                return False
    return True
