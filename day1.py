import functools
from math import floor

# lock parameters
min_num = 0
max_num = 99
lock_positions = len(range(min_num, max_num+1))

# game parameters
start_at = 50

# variables
positions = [start_at]
clicks = 0


@functools.lru_cache(maxsize=None)
def get_position(abs_position: int = start_at) -> int:
    return int(abs_position % 100)


def count_clicks(position, move):
    rounds = abs(move)//lock_positions

    if position == 0:
        return rounds

    remaining_move = move - rounds * lock_positions if move > 0 else move + rounds * lock_positions
    new_position = position + remaining_move
    
    if move > 0: # move right
        click = 1 if new_position > 99 else 0
    else: # move left
        click = 1 if new_position < 1 else 0


    return click + rounds


with open('input/day1/input1.txt', 'r', encoding='utf-8') as file:
    for txt_line in file:
        line = txt_line.strip()
        move = int(line[1:]) if line[0] == 'R' else -int(line[1:])
        positions.append(get_position(positions[-1]+move))
        clicks += count_clicks(positions[-2], move)


print(f"positions: {positions}")
print(f"clicks: {clicks}")