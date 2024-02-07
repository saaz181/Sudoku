# Killer Sudoku Solver

## CSP Model | Phase 1
### Variables: 
Variables represent the unknowns in the puzzle. In this case, we have a variable for each cell in the grid. Let's denote the variables as `X[i, j]`, where `i` represents the row number **(1 to 9)** and `j` represents the column number **(1 to 9)**.

### Domains: 
The domains represent the possible values that each variable can take. In classic Sudoku, the domains are the numbers **1 to 9**. However, in Killer Sudoku, we need to consider the additional constraints imposed by the cages. For each variable `X[i, j]`, the domain is `{1, 2, 3, 4, 5, 6, 7, 8, 9}`.

### Constraints:
Uniqueness constraint: No number can repeat within a row, a column, or a 3x3 block. This constraint is the same as in classic Sudoku.
Sum constraint: The sum of numbers in each cage must be equal to the number in the upper left corner of the cage. This constraint ensures that the sum rule is satisfied.

### Formulating the CSP model: 
The CSP model consists of the variables, domains, and constraints. In this case, we have `81` variables (`X[i, j]` for `i` from 1 to 9 and `j` from 1 to 9), each with the domain `{1, 2, 3, 4, 5, 6, 7, 8, 9}`. The constraints include the uniqueness constraint (no repetitions in rows, columns, or `3x3` blocks) and the sum constraint for each **cage**.


### Algorithm: 
Various algorithms can be used to solve the Killer Sudoku CSP model. One commonly used algorithm is the backtracking algorithm with constraint propagation. This algorithm systematically assigns values to variables while respecting the constraints and backtracks when a constraint violation is encountered.

### Killer Sudoku Solver: 
Apply the chosen algorithm to search for a solution to the CSP model. The algorithm will recursively assign values to variables, propagate constraints, and backtrack when necessary until a valid solution is found or all possibilities are exhausted.
---

## Overview

The Killer Sudoku Solver project is a Python application designed to solve Killer Sudoku puzzles using backtracking and constraint satisfaction techniques. The project includes modules for parsing Sudoku puzzles, rendering them on a graphical interface using Pygame, and implementing algorithms to solve them.

## File Structure

```
- BELL.tff
- images.png
- main.py
- screen.py
- solver.py
- test_case.txt
```

## Files Description

### 1. BELL.tff
   - **Description**: Font file used for rendering text in the graphical interface.
   - **Usage**: Imported in the `screen.py` module for rendering text.

### 2. images.png
   - **Description**: Image file used as an icon for the Pygame window.
   - **Usage**: Set as the window icon in the `main.py` module.

### 3. main.py
   - **Description**: Main script orchestrating the entire project.
   - **Functionality**:
     - Imports functionality from the `solver` module and defines classes like `Cage`.
     - Handles user input for Sudoku puzzle and cage configurations.
     - Initializes the Pygame window and starts the solving process.
   - **Dependencies**: Depends on `solver.py` and `screen.py` modules for puzzle solving and graphical rendering.

### 4. screen.py
   - **Description**: Module responsible for rendering Sudoku grids and cages on the Pygame window.
   - **Functionality**:
     - Defines the `Screen` class with methods for drawing the Sudoku grid, numbers, and cages with borders.
     - Implements a function for drawing dashed lines.
   - **Dependencies**: Depends on Pygame for graphical rendering.

### 5. solver.py
   - **Description**: Module containing algorithms for solving Killer Sudoku puzzles.
   - **Functionality**:
     - Defines functions for solving puzzles using backtracking and constraint satisfaction techniques.
     - Checks the validity of numbers based on Sudoku rules and cage constraints.
     - Applies heuristics such as Minimum Remaining Values (MRV) and Least Constraining Value (LCV).
   - **Dependencies**: No external dependencies.

### 6. test_case.txt
   - **Description**: File containing test cases for validating the solver
   - **Functionality**: May include sample Sudoku puzzles for testing the solver's functionality.

## Usage

1. Ensure all files are in the same directory.
2. Run `main.py` to start the application.
3. Input the Sudoku puzzle and cage configurations as prompted.
4. The application will display the solution on the Pygame window.

## Contributors

- Amin Reza Najafinia
- Ali Alavizadeh
- Paria Razavi