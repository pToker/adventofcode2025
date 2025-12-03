from functools import lru_cache
import re

def find_fake_id(number: str, search_scope: str):
    pass

@lru_cache
def get_devisors(number_string: str):
    l = len(number_string)
    devisors = [l]

    for i in range (2,int(l)//2+1):
        if l%i == 0: # can be devided by i
            devisors.append(i)

    return devisors


def split_string_into_n_parts(s, n):
    chunk_size = len(s) // n
    remainder = len(s) % n # should always be 0 due to preprocessing in `devisors` but on
    parts = []
    start = 0
    for i in range(n):
        # Adjust chunk size for the first 'remainder' parts to distribute extra characters
        size = chunk_size + (1 if i < remainder else 0)
        parts.append(s[start:start + size])
        start += size
    return parts   

with open('input/day2/input1.txt', 'r', encoding='utf-8') as file:
    raw_input = file.readlines()[0].strip()
    # print(f"{raw_input=}")

    ranges = raw_input.split(',')

    invalid_ids = []


    for num_range in ranges:
        num_range = num_range.split('-')
        range_start = int(num_range[0])
        range_end = int(num_range[1])
        
        # print(f"Looking for duplicats in {num_range=} (so between {range_start=} and {range_end=}")

        for number in range(range_start,range_end+1):
            if number < 11:
                continue
            str_num = str(number)
            n = digits = len(str_num)

            splitters = reversed(get_devisors(str_num))
            for i in splitters:
                parts = split_string_into_n_parts(str_num, i)
                if len(set(parts)) == 1:  # Returns True if all parts are identical
                    invalid_ids.append(number)
                    break


print(invalid_ids)
print(f"{len(invalid_ids)=}")
print(f"{len(set(invalid_ids))=}") # just in case there would be duplicates for some reason

print(f"sum of invalid IDs: {sum(invalid_ids)=}")

# =73694270733 is too high