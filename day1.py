import requests
import functools


@functools.lru_cache(maxsize=None)
def get_position(position):
    return position % 100

start_at = 50
positions = [start_at]
zeroes = 0

# read input file input/day1/input1.txt line by line
with open('input/day1/input1.txt', 'r', encoding='utf-8') as file:
    for txt_line in file:
        line = txt_line.strip()
        position = get_position(positions[-1] + (int(line[1:]) if line[0] == 'R' else -int(line[1:])))
        positions.append(position)
        zeroes += 1 if position == 0 else 0
       

# print(f"positions: {positions}")
print(f"zeroes: {zeroes}")


############################ part 2 #########################################################

# c u later