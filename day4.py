
# The forklifts can only access a roll of paper if there are *fewer than four rolls of paper in the eight adjacent positions*.
# If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.

warehouse = []
accessible = 0
def range_count(y: int, x: int, neigh_l_r: set):
    values = []
    l = x-neigh_l_r[0]
    r = x+neigh_l_r[1]
    for pos in range(x if l < 0 else l, (x if r > w-1 else r)+1):
        values.append(warehouse[y][pos])
    return sum(values)

def count_neighbours(x:int, y:int) -> int:
    # print(f"coordinates {x=},{y=} contain value {warehouse[y][x]=}")
    neighbours = []
    if y > 0: # get row above
        neighbours.append(range_count(y=y-1,x=x,neigh_l_r=(1,1)))
    neighbours.append(range_count(y=y,x=x,neigh_l_r=(1,1))-1) # -1: do not count myself as a neighbour
    if y < h-1: # get row below
        neighbours.append(range_count(y=y+1,x=x,neigh_l_r=(1,1)))

    return sum(neighbours)

with open('input/day4/input1.txt', 'r', encoding='utf-8') as file:
    for txt_line in file:
        line = txt_line.strip()
        # change '.' to 0 and '@' to 1 for readability
        warehouse.append([0 if x == '.' else 1 for x in line])

w = len(warehouse[0])
h = len(warehouse)
x_range = range(0,w)
y_range = range(0,h)

for idx, line in enumerate(warehouse):
    for ix, spot in enumerate(line):
        if spot == 0: # skip empty spots
            continue
        print(f"{spot} at {ix=},{idx=} has {count_neighbours(ix, idx)=}")
        if count_neighbours(ix, idx) < 4:
            accessible += 1

print(f"{accessible=} @ are accessible")