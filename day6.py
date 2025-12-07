import operator
import re
from numpy import invert
import pandas as pd
import math

splitty = re.compile(r'\s+')
lines = []
line_strings = []
math_blocks = []
result = 0

def operate(row, operations):
    value = operations[row.name]
    match value:
        case '*':
            return math.prod(row)
        case '+':
            return sum(row)

def maxlen(row):
    return max(len(str(row[0])),len(str(row[1])),len(str(row[2])),len(str(row[3])))


def do_the_math(cumbers, operator):
    match operator:
        case '*':
            return math.prod(cumbers)
        case '+':
            return sum(cumbers)

def reorder_numbers(block):
    numbers = [''] * len(block[0])
    for h_num in block:
        for i, digit in enumerate(h_num[::-1]):
            try:
                if digit != '': numbers[i] +=  digit
            except IndexError:
                print(f"{i=} of {digit=} in {block=} is invalid. {numbers=}")
    return [int(number) for number in numbers]





with open('input/day6/input1.txt', 'r', encoding='utf-8') as file:
    for txt_line in file:
        if txt_line.strip() != "":
            line = txt_line.rstrip("\n")
            line_strings.append(line)
            elements_of_line = [int(x) if x.isdigit() else x for x in re.split(splitty,line)]
            lines.append(elements_of_line)

numbers = pd.DataFrame(data=lines[0:-1]).T.dropna()


operations = pd.Series([line for line in lines[-1] if line != ''], index=numbers.index)

# numbers = numbers.assign(result=ops[operations](numbers[0],numbers[1],numbers[2],numbers[3])) # does not work
numbers['result'] = numbers.apply(lambda row: operate(row, operations) , axis=1)
numbers['maxlen'] = numbers.apply(lambda row: maxlen(row), axis=1)
str_lengths = numbers['maxlen'].to_list()

print("Pandas Dataframe to get the max-length of the ranges")
print(numbers.head())
print(numbers.describe())
print(numbers.info())
print(f"Existing operations in data: {operations.unique()}")

# result for day 6.1
print(f"Result for day 6.1: {numbers['result'].sum()}")
print(str_lengths, len(str_lengths))


# prepare the data for 6.2
for idx, length in enumerate(str_lengths):
    math_block = []
    for ix, line in enumerate(line_strings):
        math_block.append(line[:length])
        line_strings[ix] = line_strings[ix][length+1:] # cut the number off the string
    math_blocks.append(math_block)


for idx, block in enumerate(math_blocks):
    cumbers = reorder_numbers(block[:-1])
    operator = block[-1].strip()

    try:
        result += do_the_math(cumbers,operator)
    except TypeError:
        print(f"using {idx=} {block=} {cumbers=} and {operator=} we get {do_the_math(cumbers,operator)=}")
        print(f"previous record is {math_blocks[idx-1]=}")

print(f"Result for day 6.2: {result=}")