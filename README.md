# Soduko

## CSP Model
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