import math
from helpers.timer import timeit

with open('day6/input.txt', 'r') as f:
    grid = []
    for line in f:
        row = line.split()
        row = [int(x) if x.isdigit() else x for x in row]
        grid.append(row)

row_depth = len(grid)
column_depth = len(grid[0])

# Part 1

@timeit
def calculate_columns(grid):
    total = 0
    i = 0
    while i < column_depth:
        col = [row[i] for row in grid]
        c = col.pop()
        if c == '*':
            column_total = (math.prod(col))
        elif c == '+':
            column_total = sum(col)
        total += column_total        
        i += 1
    print(f'Part 1 solution: {total}')

calculate_columns(grid)