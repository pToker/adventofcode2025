
with open('input/day2/input1.txt', 'r', encoding='utf-8') as file:
    raw_input = file.readlines()[0].strip()
    # print(f"{raw_input=}")

    ranges = raw_input.split(',')
    # print(f"{ranges=}")

    invalid_ids = []


    for num_range in ranges:
        num_range = num_range.split('-')
        range_start = int(num_range[0])
        range_end = int(num_range[1])
        
        # print(f"Looking for duplicats in {num_range=} (so between {range_start=} and {range_end=}")

        for number in range(range_start,range_end+1):
            digits = len(str(number))

            if digits%2 == 1: # only even nubers are potentilly affected so we skipp odd ones
                continue
            
            # print(f"{str(number)[0:(digits//2-1)]=} == {str(number)[(digits//2+1):]=}")
            if str(number)[0:(digits//2)] == str(number)[(digits//2):]:
                # print(f"{number=} is invalid")
                invalid_ids.append(number)

            if range_end == number:
                # print(f"Reached the end with {number=}")

        

print(f"sum of invalid IDs: {sum(invalid_ids)=}")