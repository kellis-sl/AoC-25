from collections import deque
import re
from helpers.timer import timeit

def parse_puzzle_line(line):
    
    # Extract the initial state between [ ]
    state_match = re.search(r'\[(.*?)\]', line)
    if not state_match:
        return None
    
    initial_state = state_match.group(1).replace('#', '0').replace('.', '0')
    final_state = state_match.group(1).replace('#', '1').replace('.', '0')
    
    # Extract all tuples between ( )
    operations = []
    for match in re.finditer(r'\(([0-9,\s]+)\)', line):
        nums = [int(x.strip()) for x in match.group(1).split(',')]
        operations.append(tuple(nums))
        
    return {
        'initial_state': initial_state,
        'final_state': final_state,
        'operations': operations,
    }

def read_puzzles_from_file(filename):
    #Read puzzles from a file, one per line.
    puzzles = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            puzzle = parse_puzzle_line(line)
            puzzles.append(puzzle)
    return puzzles

def apply_operation(state, op):
    #Toggle bits specified in the operation tuple
    new_state = list(state)
    for bit_pos in op:
        new_state[bit_pos] = '1' if new_state[bit_pos] == '0' else '0'
    return ''.join(new_state)


@timeit
def find_min_operations(initial, target, operations):
    """
    Find minimum number of operations to transform initial to target state.
    Uses BFS to explore all possible sequences.
    """
    if initial == target:
        return 0, []
    
    queue = deque([(initial, [], [])])
    visited = {initial}
    
    while queue:
        state, ops_used, op_indices = queue.popleft()
        
        # Try each operation
        for i, op in enumerate(operations):
            new_state = apply_operation(state, op)
            
            if new_state == target:
                return len(ops_used) + 1, ops_used + [op]
            
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, ops_used + [op], op_indices + [i]))
    
    return -1, []  # No solution found

puzzles = read_puzzles_from_file('day10/input')

total_presses = 0

for i, puzzle in enumerate(puzzles, 1):
    print(f"\nPuzzle {i}:")
    print(f"Initial state: {puzzle['initial_state']}")
    print(f"Operations: {puzzle['operations']}")
    
    target = puzzle['final_state']
    min_ops, solution = find_min_operations(
        puzzle['initial_state'], 
        puzzle['final_state'], 
        puzzle['operations']
    )

    total_presses += min_ops
    
    print("-"*60)

print(f'Total button presses: {total_presses}')
