# answer 1: 635
# answer 2: submitted 369761800782619

fresh = []
fresh_ids = []
n_total_fresh_ids = 0
inventory = set()
overlaps = 1

# data preparation
with open('input/day5/input1.txt', 'r', encoding='utf-8') as file:
    for txt_line in file:
        line = txt_line.strip()
        if line == '': continue # ignore the empty line(s)

        id = line.split('-')
        match len(id):
            case 1: # no split -> id
                inventory.add(int(id[0]))
            case 2: # range of ids -> fresh stuff
                fresh.append([int(id[0]),int(id[1])])


for id in inventory:
    for area in fresh:
        if area[0] <= id <= area[1]:
            fresh_ids.append(id)
            break

print(fresh_ids)
print(f"{len(fresh_ids)=}")

while overlaps > 0:
    overlaps = 0
    for idx, area in enumerate(fresh): # is wrong because I had chosen to ignore overlaps so far
        for ix, checkarea in enumerate(fresh):
            if idx == ix: continue # do not check against yourself
            if checkarea[0] <= area[0] <= checkarea[1] or checkarea[0] <= area[1] <= checkarea[1]:
                area[0] = min(area[0],checkarea[0])
                area[1] = max(area[1],checkarea[1])
                overlaps += 1
                fresh[idx]=area
                fresh.pop(ix)
                break
        
        else:
            continue
        break
            

for i in fresh:
    n_total_fresh_ids += i[1]-i[0]+1

print(f"total fresh IDs: {n_total_fresh_ids=}")

