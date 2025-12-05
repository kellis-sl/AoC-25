import time

s = time.time()
with open('values.txt', 'r') as file:
    batteries = [line.strip() for line in file if line.strip()]
e = time.time()
print(f"Pre=process took{e - s} seconds")

# Part v1
def find_largest_pair(number, index=0, max_pair="00"):   
    length = len(number)

    if index >= length - 1:
        return max_pair
    
    for j in range(index + 1, length):
        pair = number[index] + number[j]
        if pair > max_pair:
            max_pair = pair

    return find_largest_pair(number, index + 1, max_pair)

def calculate_joltage(batteries):
    return sum(int(find_largest_pair(battery)) for battery in batteries)

s = time.time()
print(calculate_joltage(batteries))
e = time.time()
print(f"calculate_joltage_1.1 took {e - s} seconds")

# Part v1.2

def highest_two_digit(series: str) -> int:
    max_num = -1
    for i in range(len(series)):
        for j in range(i + 1, len(series)):
            num = int(series[i] + series[j])
            if num > max_num:
                max_num = num
    return max_num

def calculate_joltage_part1(batteries):
    return sum(highest_two_digit(battery) for battery in batteries)

s = time.time()
print(calculate_joltage_part1(batteries))
e = time.time()
print(f"calculate_joltage_1.2 took {e - s} seconds")

# Part 2

def highest_n_digit(series: str, n: int) -> str:
    result = []
    start = 0
    for i in range(n):
        remaining = n - i - 1
        end = len(series) - remaining
        max_digit = max(series[start:end])
        position = series.index(max_digit, start, end)
        result.append(max_digit)
        start = position + 1
    return ''.join(result)

def calculate_joltage_part2_general(batteries, n):
    return sum(int(highest_n_digit(battery, n)) for battery in batteries)

s = time.time()
print(calculate_joltage_part2_general(batteries, 12))
e = time.time() 

print(f"calculate_joltage_2 took {e - s} seconds")