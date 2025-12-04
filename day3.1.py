amount_of_batteries = 12
line_length = 100
joltage = []

def get_highest_digit(number:str, start_from: int=0, up_to=None):
    highest_number = max(number[start_from:up_to])
    ix = start_from + number[start_from:up_to].index(highest_number)
    return ix, highest_number
    


with open('input/day3/input1.txt', 'r', encoding='utf-8') as file:
    n_line = 0
    for txt_line in file:
        n_line += 1
        line = txt_line.strip()
        line_joltage = 0

        for i in range(0,amount_of_batteries): # 0 - 11
            ix, prev_num = get_highest_digit(line, 0 if i == 0 else ix+1, -(amount_of_batteries-1-i) if (amount_of_batteries-1-i) != 0 else None)
            line_joltage += 10**(amount_of_batteries-1-i) * int(prev_num)
            if ix + amount_of_batteries-1-i >= line_length-1: # add all remaining numbers once the amount of remaining batteries is equal to the amount of needed batteries
                if ix < line_length-1:
                    line_joltage += int(line[ix+1:])
                break
            
        joltage.append(line_joltage)

        print(f"{line=}")
        print(f"{joltage=}")


print(sum(joltage))