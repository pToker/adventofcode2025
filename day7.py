# Ray shoots from 'S'
# if you have a splitty (^), which gets a hitty, you have to county

from queue import Empty


source = 'S'
splitter = '^'
splitter_hit = '+'
beam = '|'
space = '.'

line_strings = []
n_line = 0
hit_splitters = 0

def get_char_by_position(lol, line: int = 0, position: int = 0): # lol = list of lists
    if lol != None:
        if 0 <= line <= len(lol):
            if 0 <= line < len(lol) and 0 <= position < len(lol[line]):
                return lol[line][position]
    return None  # ran through the function without error but did not find (anything) at given location


with open('input/day7/input1.txt', 'r', encoding='utf-8') as file:
    for txt_line in file:
        if txt_line.strip() != "":
            line = txt_line.rstrip("\n")
            new_line = ''
            # process
            for ix, pos in enumerate(line):
                if get_char_by_position(line_strings,n_line-1,ix) in [source,beam] or get_char_by_position(line_strings,n_line-1,ix-1) == splitter_hit or get_char_by_position(line_strings,n_line-1,ix+1) == splitter_hit:
                    if pos == space:
                        new_line += beam
                    elif pos == splitter:
                        hit_splitters += 1
                        new_line += splitter_hit
                else:
                    new_line += pos

            line_strings.append(new_line)
            n_line += 1


for line in line_strings:
    print(line)

print(f"Splitters hit: {hit_splitters=}")