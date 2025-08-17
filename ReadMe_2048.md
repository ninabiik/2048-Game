This repository contains a small, **console-based** demo that performs 2048-style merge operations on a 4×4 grid and prints the result. It includes movement functions for **left, right, up, down** and a `merge` routine that combines adjacent equal tiles.

> ⚠️ This is a minimal logic demo (no full game loop, no random tile spawns, no scoring, no win/lose detection).

---

## What it does

- Initializes a 4×4 grid
- Provides movement functions:
  - `move_left` / `move_right`
  - `move_up` / `move_down`
- Merges adjacent equal numbers in the direction of the move
- Prints the grid before and after a sample **left** move

---

## Requirements

- Python **3.7+**

No external libraries are required.

---

## How to run

Save your code as `main.py` (or any name) and run:

```bash
python main.py
```
Example
Given the main() in your script:

```
grid = initialize_grid()
grid[0] = [4, 0, 0, 4]
grid[1] = [32, 16, 16, 32]
grid[2] = [512, 1024, 1024, 256]
grid[3] = [2, 4, 8, 16]

print("Initial grid:")
print_grid(grid)

print("\\nPerforming move: left")
grid = move_left(grid)
print("\\nUpdated grid:")
print_grid(grid)
```
Expected output in yaml (conceptual):

```
Initial grid:
4 0 0 4
32 16 16 32
512 1024 1024 256
2 4 8 16

Performing move: left

Updated grid:
4 4 0 0
32 32 32 0
512 2048 256 0
2 4 8 16
```

File overview
- initialize_grid() – Creates a zero-filled 4×4 grid. 
- print_grid(grid) – Prints the grid to stdout. 
- merge(row) – Core merge routine used by all movement functions. 
- move_left(grid) – Applies merge to each row. 
- move_right(grid) – Reverses rows, merges, reverses back. 
- move_up(grid) – Transposes, merges rows, transposes back. 
- move_down(grid) – Transposes, reverses rows, merges, reverse & transpose back. 
- main() – Demo: sets up a test grid, performs a left move, prints results.

Possible improvements

- Add a compression step before merging to emulate classic 2048 behavior exactly 
- Implement random tile spawns (2 or 4) after each move 
- Track score and detect win/lose states 
- Add a keyboard-controlled loop or GUI

License
MIT
```
path = "/mnt/data/README_2048_demo.md"
with open(path, "w", encoding="utf-8") as f:
f.write(readme)

print(path)
```