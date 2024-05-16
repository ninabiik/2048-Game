import random

def initialize_grid():
    grid = [[0] * 4 for _ in range(4)]
    return grid

def print_grid(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))

def merge(row):
    merged_row = []
    i = 0
    while i < len(row):
        if row[i] == 0:
            i += 1
            continue
        if i == len(row) - 1:
            merged_row.append(row[i])
            break
        if row[i] == row[i + 1]:
            merged_row.append(row[i] * 2)
            i += 2
        else:
            merged_row.append(row[i])
            i += 1
    while len(merged_row) < 4:
        merged_row.append(0)
    return merged_row

def move_left(grid):
    for i in range(4):
        grid[i] = merge(grid[i])
    return grid

def move_right(grid):
    for i in range(4):
        grid[i] = merge(grid[i][::-1])[::-1]
    return grid

def move_up(grid):
    transposed_grid = [list(row) for row in zip(*grid)]
    for i in range(4):
        transposed_grid[i] = merge(transposed_grid[i])
    grid = [list(row) for row in zip(*transposed_grid)]
    return grid

def move_down(grid):
    transposed_grid = [list(row) for row in zip(*grid)]
    for i in range(4):
        transposed_grid[i] = merge(transposed_grid[i][::-1])[::-1]
    grid = [list(row) for row in zip(*transposed_grid)]
    return grid

def main():
    grid = initialize_grid()
    grid[0] = [4, 0, 0, 4]
    grid[1] = [32, 16, 16, 32]
    grid[2] = [512, 1024, 1024, 256]
    grid[3] = [2, 4, 8, 16]

    print("Initial grid:")
    print_grid(grid)

    print("\nPerforming move: left")
    grid = move_left(grid)
    print("\nUpdated grid:")
    print_grid(grid)

if __name__ == "__main__":
    main()
