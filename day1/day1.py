def process_series(series): # ['L50', 'R30', L120, R80, ...]   
    x = 50
    zero_count = 0
    
    for value in series:
        # Extract the direction (L or R) and the number
        direction = value[0]
        number = int(value[1:])

        print(f"Processing value: {value}, Current x: {x}")

        if number > 100:
            wraps = number // 100
            zero_count += wraps
            number = number % 100

        print(f"After handling wraps, number: {number}, zero_count: {zero_count}")

        if x == 0:        
            if direction == 'L':
                x = x - number
                if x < 0:
                    x = 100 + x
            elif direction == 'R':
                x = x + number
                if x > 100:
                    x = x - 100  # This is equivalent to 0 + (x - 100)
        else:
            if direction == 'L':
                x = x - number
                if x < 0:
                    x = 100 + x
                    zero_count += 1
            elif direction == 'R':
                x = x + number
                if x > 100:
                    x = x - 100  # This is equivalent to 0 + (x - 100)
                    zero_count += 1
        
        if x == 100:
            x = 0
        
        # Check if x equals 0 after processing this value
        if x == 0:
            zero_count += 1

        print(f"Updated x: {x}, Current zero_count: {zero_count}")
    
    return zero_count, x

with open('values.txt', 'r') as file:
    series = [line.strip() for line in file if line.strip()]
    line_count = len(series)

# Example usage
count, final_x = process_series(series)
print(f"Number of lines processed: {line_count}")
print(f"x = 0 occurred {count} times")
print(f"Final value of x: {final_x}")