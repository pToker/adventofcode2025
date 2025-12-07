import re
import pandas as pd
import math

splitty = re.compile(r'\s+')
lines = []

def operate(row, operations):
    value = operations[row.name]
    match value:
        case '*':
            return math.prod(row)
        case '+':
            return sum(row)


with open('input/day6/input1.txt', 'r', encoding='utf-8') as file:
    for txt_line in file:
        line = txt_line.strip()
        elements_of_line = [int(x) if x.isdigit() else x for x in re.split(splitty,line)]
        lines.append(elements_of_line)

numbers = pd.DataFrame(data=lines[0:-1]).T


operations = pd.Series(lines[-1], index=numbers.index)

# numbers = numbers.assign(result=ops[operations](numbers[0],numbers[1],numbers[2],numbers[3])) # does not work
numbers['result'] = numbers.apply(lambda row: operate(row, operations) , axis=1)

print(numbers.head())
print(operations.unique())

print(numbers['result'].sum())