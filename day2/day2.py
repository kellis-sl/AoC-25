with open('values.txt', 'r') as f:
    ids = f.read()
    ranges = []
    for range_str in ids.split(','):
        start, end = range_str.split('-')
        include_end = int(end) + 1
        ranges.append((int(start), include_end))

def get_ids(ranges):
    invalid_ids = []
    for value in ranges:
        for id in range(value[0], value[1]):
            id_str = str(id)
            length = len(id_str)

            if len(id_str) > 1 and checkSameDigits(id):
                print(f"Invalid ID found (same digits): {id}")
                invalid_ids.append(id)

            else:            
                for pattern_len in range(2, length // 2 + 1):
                    if length % pattern_len == 0:           
                        pattern = id_str[:pattern_len]
                                    
                        if pattern * (length // pattern_len) == id_str:
                            print(f"Invalid ID found: {id}")
                            invalid_ids.append(id)
                            break                  

    return sum(invalid_ids)

def checkSameDigits(N) :
    # Find the last digit
        digit = N % 10

        while (N != 0) :

            # Find the current last digit
            current_digit = N % 10
            # Update the value of N
            N = N // 10

            # If there exists any distinct
            # digit, then return No
            if (current_digit != digit) :
                return False

        # Otherwise, return Yes
        return True

print(get_ids(ranges))