import os
import time
from random import randint
from pprint import pprint


def random_habitat_state(width, height):
    return [[randint(0, 1) for w in range(width)] for h in range(height)]


def render(grid):
    print("+" + "-" * len(grid[0]) + "+")
    for row in grid:
        print("|" + ''.join(['#' if cell == 1 else '.' for cell in row]) + "|")
    print("+" + "-" * len(grid[0]) + "+")


def find_neighbors(grid, x, y):
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= x + i < len(grid) and 0 <= y + j < len(grid[0]):
                neighbors.append(grid[x + i][y + j])
    return neighbors


def calc_state(grid, x, y):
    neighbors = find_neighbors(grid, x, y)
    alive = sum(neighbors)
    dead = len(neighbors) - alive
    if grid[x][y] == 1:
        if alive < 2 or alive > 3:
            return 0
        else:
            return 1
    elif grid[x][y] == 0:
        if alive == 3:
            return 1
        else:
            return 0


def custom_habitat_loader():
    habitat = open("habitat.txt", "r")
    return [[int(cell) for cell in row.strip()] for row in habitat]


def game_loop(grid):
    cycle = 0
    max_cycles = 100  # Set a maximum number of iterations
    while game_state and cycle < max_cycles:
        cycle += 1
        new_grid = []
        for x in range(len(grid)):
            new_row = []
            for y in range(len(grid[0])):
                state = calc_state(grid, x, y)
                new_row.append(state)
            new_grid.append(new_row)
        old_grid = grid
        grid = new_grid

        os.system('cls')  # Clear the screen (Windows)
        print(f"Cycles: {cycle}")
        render(new_grid)

        # Optional: Add a condition to break the loop if the grid stabilizes
        if old_grid == new_grid:
            print(" Life Of Game ")
            break

        time.sleep(1)  # Add a delay of 1 second


# Initialize the game state
game_state = True

# Initial grid setup
# grid = custom_habitat_loader("habitat.txt")
# print("Initial Grid:")
# render(grid)
# print(render(random_state(5, 5)))
cycle = 0
max_cycles = 100  # Set a maximum number of iterations
grid = random_habitat_state(150, 50)
game_loop(grid)
