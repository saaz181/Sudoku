import pygame.display
from solver import *

class Cage:
    def __init__(self, cells, value):
        self.cells = cells  # List of cells belonging to the cage
        self.value = value  # Expected sum of numbers in the cage
        self.color = self.random_color()  # Assigning a random color to the cage

    # Function to generate a random color
    def random_color(self):
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


# Function to get Sudoku matrix input from the user
def get_matrix_input():
    # Create a 2D array to store the input
    input_arr = []
    # Iterate through 9 rows
    for _ in range(9):
        row_input = input().strip().split()  # Get input for each row and split it into individual numbers
        # Convert the input numbers from string to integers and append them to the 2D array
        input_arr.append([int(num) for num in row_input])
    # Return the input array
    return input_arr


# Function to get input for cages from the user
def get_cages_input():
    num_cages = int(input())  # Get the number of cages from the user
    cages = []  # Initialize list to store Cage objects
    for _ in range(num_cages):
        data = input("").split(" > ")  # Split input data for each cage
        cells = list(map(int, data[0].split()))  # Get cells belonging to the cage
        value = int(data[1])  # Get the expected sum of numbers in the cage
        cages.append(Cage(cells, value))  # Create a Cage object and append it to the list
    return cages  # Return the list of Cage objects


# Function to run the main loop of the program
def run(Scr):
    # Main loop
    running = True
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode(Scr.size)  # Set up Pygame window
    pygame.display.set_caption("Sudoku Solver")  # Set window title
    icon = pygame.transform.scale(pygame.image.load('images.png'), (32, 32))  # Load and set window icon
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()  # Pygame clock for controlling frame rate
    while running:
        # Control the frame rate
        clock.tick(60)
        for event in pygame.event.get():  # Get events from Pygame event queue
            if event.type == pygame.QUIT:  # If the user closes the window
                running = False

        screen.fill(WHITE)  # Fill the screen with white color
        Scr.draw_grid(screen)  # Draw Sudoku grid on the screen
        if not solve(Scr, screen):  # Solve the Sudoku puzzle
            print("Not Solvable")  # Print message if puzzle is not solvable
            quit()
        pygame.display.flip()  # Update the display

    pygame.quit()


# Get input for Sudoku matrix and cages from the user
sudoku = get_matrix_input()
cages = get_cages_input()

# Create a Screen object with the provided cages and set the Sudoku matrix
Scr = Screen(cages)
Scr.set_sudoku(sudoku)

# Run the main loop of the program
run(Scr)
