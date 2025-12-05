from typing import List
from helpers.timer import timeit

with open('day5/input.txt', 'r') as file:
    input = [line.strip() for line in file if line.strip()]

@timeit
def get_ranges(input):
    return[list(map(int, item.split('-'))) for item in input if '-' in item]

@timeit
def get_ids(input):
    return[int(item) for item in input if '-' not in item]

ranges = get_ranges(input)
ids = get_ids(input)

# Part 1
@timeit
def check_id_in_ranges(ids, ranges):
    count = 0
    for id in ids:
        #print(f'Checking id: {id}')
        status = []
        for range in ranges:
            if range[0] <= id <= range[1]:
                status.append('x')
        if 'x' in status:
            #print('Fresh')
            count += 1
    return(count)

# Cleaner function
@timeit
def check_id_in_ranges_2(ids, ranges):
    count = 0
    for item_id in ids:
        for start, end in ranges:
            if start <= item_id <= end:
                count += 1
                break  # Stop checking once we find a match
    return count

print(f'Part 1 Solution: {check_id_in_ranges_2(ids, ranges)}')

# Part 2
@timeit
def consolidate_ranges(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []
    # Sort the intervals based on the starting points
    intervals.sort(key=lambda x: x[0])
    merged_intervals = [intervals[0]]
    for current in intervals[1:]:
        last_merged = merged_intervals[-1]
        # If the current interval overlaps with the last merged interval, merge them
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # Otherwise, add the current interval to the merged list
            merged_intervals.append(current)
    return merged_intervals

@timeit
def count_range_size(ranges):
    total_size = 0
    for start, end in ranges:
        include_end = end + 1
        total_size = total_size + (include_end - start)
    return(total_size)

ranges = (consolidate_ranges(ranges))
print(f'Part 2 solution: {count_range_size(ranges)}')
