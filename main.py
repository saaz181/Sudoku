from screen import *


class Cage:
    def __init__(self, cells, value):
        self.cells = cells
        self.value = value
        self.color = self.random_color()

    # Function to generate a random color
    def random_color(self):
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def get_matrix_input():
    # Create a 2D array to store the input
    input_arr = []
    # Iterate through 9 rows
    for _ in range(9):
        row_input = input().strip().split()
        # Convert the input numbers from string to integers and append them to the 2D array
        input_arr.append([int(num) for num in row_input])
    # Print the input array
    return input_arr


def get_cages_input():
    num_cages = int(input())
    cages = []
    for _ in range(num_cages):
        data = input("").split(" > ")
        cells = list(map(int, data[0].split()))
        value = int(data[1])
        cages.append(Cage(cells, value))
    return cages


def run(Scr, cages):
    # Main loop
    running = True
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode(Scr.size)
    clock = pygame.time.Clock()
    while running:
        # Control the frame rate
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        Scr.draw_grid(screen, cages)
        Scr.draw_numbers(screen)
        pygame.display.flip()

    pygame.quit()


Scr = Screen()
cage1 = Cage([11, 12, 22], 8)
cage2 = Cage([45, 46, 56, 57, 58], 22)
cage_lists = [cage1, cage2]
Scr.set_sudoku([[6, 0, 9, 0, 0, 7, 0, 3, 0],
                [0, 0, 0, 0, 9, 0, 0, 0, 6],
                [0, 2, 0, 0, 0, 3, 9, 4, 0],
                [0, 0, 0, 0, 8, 2, 7, 0, 0],
                [2, 0, 8, 0, 7, 0, 0, 0, 3],
                [0, 0, 0, 9, 1, 6, 0, 8, 0],
                [0, 0, 2, 0, 0, 0, 0, 1, 4],
                [3, 0, 4, 6, 5, 0, 8, 0, 0],
                [1, 0, 5, 0, 0, 9, 0, 0, 0]])
run(Scr, cage_lists)
