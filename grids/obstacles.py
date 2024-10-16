import numpy as np
import matplotlib.pyplot as plt
import random

def s_shape(grid, size):
    while True:
        x, y = random.randint(0, size - 2), random.randint(1, size - 2)  # Adjusting the range to avoid index errors
        if (grid[x][y] == 0 and grid[x][y - 1] == 0 and 
                grid[x + 1][y - 1] == 0 and grid[x + 1][y - 2] == 0):
            grid[x][y] = 1
            grid[x][y - 1] = 1
            grid[x + 1][y - 1] = 1
            grid[x + 1][y - 2] = 1
            break
    return grid

def line_shape(grid, size):
    while True:
        x = random.randint(0, size - 4)
        y = random.randint(0, size - 1)
        if (grid[x][y] == 0 and grid[x + 1][y] == 0 and 
                grid[x + 2][y] == 0 and grid[x + 3][y] == 0):
            grid[x][y] = 1
            grid[x + 1][y] = 1
            grid[x + 2][y] = 1
            grid[x + 3][y] = 1
            break
    return grid

def l_shape(grid, size):
    while True:
        x = random.randint(0, size - 3)
        y = random.randint(0, size - 2)
        if (grid[x][y] == 0 and grid[x + 1][y] == 0 and 
                grid[x + 2][y] == 0 and grid[x + 2][y + 1] == 0):
            grid[x][y] = 1
            grid[x + 1][y] = 1
            grid[x + 2][y] = 1
            grid[x + 2][y + 1] = 1
            break
    return grid

def z_shape(grid, size):
    while True:
        x, y = random.randint(0, size - 2), random.randint(0, size - 3)
        if (grid[x][y] == 0 and grid[x][y + 1] == 0 and 
                grid[x + 1][y + 1] == 0 and grid[x + 1][y + 2] == 0):
            grid[x][y] = 1
            grid[x][y + 1] = 1
            grid[x + 1][y + 1] = 1
            grid[x + 1][y + 2] = 1
            break
    return grid

def ht_shape(grid, size):
    while True:
        x = random.randint(1, size - 2)
        y = random.randint(0, size - 2)
        if (grid[x][y] == 0 and grid[x][y + 1] == 0 and 
                grid[x - 1][y + 1] == 0 and grid[x + 1][y + 1] == 0):
            grid[x][y] = 1
            grid[x][y + 1] = 1
            grid[x - 1][y + 1] = 1
            grid[x + 1][y + 1] = 1
            break
    return grid

def four_shape(grid, size):
    while True:
        x = random.randint(0, size - 3)
        y = random.randint(0, size - 2)
        if (grid[x][y] == 0 and grid[x + 1][y] == 0 and 
                grid[x + 1][y + 1] == 0 and grid[x + 2][y + 1] == 0):
            grid[x][y] = 1
            grid[x + 1][y] = 1
            grid[x + 1][y + 1] = 1
            grid[x + 2][y + 1] = 1
            break
    return grid

def il_shape(grid, size):
    while True:
        x = random.randint(0, size - 3)
        y = random.randint(0, size - 2)
        if (grid[x][y] == 0 and grid[x][y + 1] == 0 and 
                grid[x + 1][y + 1] == 0 and grid[x + 2][y + 1] == 0):
            grid[x][y] = 1
            grid[x][y + 1] = 1
            grid[x + 1][y + 1] = 1
            grid[x + 2][y + 1] = 1
            break
    return grid

def square_shape(grid, size):
    while True:
        x = random.randint(0, size - 2)
        y = random.randint(0, size - 2)
        if (grid[x][y] == 0 and grid[x][y + 1] == 0 and 
                grid[x + 1][y + 1] == 0 and grid[x + 1][y] == 0):
            grid[x][y] = 1
            grid[x][y + 1] = 1
            grid[x + 1][y + 1] = 1
            grid[x + 1][y] = 1
            break
    return grid

def run(percent, grid_size):
    grid = np.zeros((grid_size, grid_size), dtype=int)
    shape_funcs = [s_shape, z_shape, line_shape, l_shape, ht_shape,
                   four_shape, il_shape, square_shape]

    num_shapes = int((grid_size * grid_size * percent) / 100 / 4)  # Calculate the number of shapes based on percentage
    for _ in range(num_shapes):
        func = random.choice(shape_funcs)  # Randomly select a shape function
        grid = func(grid, grid_size)

    return grid

def save_grid_to_file(grid, filename):
    with open(filename, 'w') as f:
        for row in grid:
            f.write(' '.join(map(str, row)) + '\n') 

if __name__ == "__main__":
    grid_size = 40  # Set your desired grid size here
    obstacle_percent = 15  # Set the desired percentage of obstacles
    grid = run(obstacle_percent, grid_size)
    save_grid_to_file(grid, 'grid15.txt')
    plt.imshow(grid, cmap='Greys')
    plt.title(f'Grid with {obstacle_percent}% Obstacles')
    plt.show()
