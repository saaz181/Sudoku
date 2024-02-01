import copy

from screen import *


def solve(Scr: Screen):
    for row in range(9):
        for col in range(9):
            if Scr.sudoku_grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(num, row, col, Scr):
                        Scr.sudoku_grid[row][col] = num  # Make the change
                        if solve(Scr):
                            return True  # If successful, propagate the success back up
                        Scr.sudoku_grid[row][col] = 0  # Revert the change on failure
                return False  # If no number is valid, backtrack
    return True  # If the end of the grid is reached, the puzzle is solved



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