import time

s = time.time()

with open('values.txt', 'r') as file:
    rolls = [line.strip() for line in file if line.strip()]
    grid = [rolls]
    print(grid)
e = time.time()
print(f"Pre=process took{e - s} seconds")