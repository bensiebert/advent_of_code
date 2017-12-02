from itertools import combinations

def convert_to_ints(file_input):
    for line in file_input:
        yield [int(num) for num in line.split()]

def calc_checksum(spreadsheet, checksum_func):
    return sum(checksum_func(line) for line in spreadsheet)

def diff_of_min_and_max(nums):
    return max(nums) - min(nums)

def div_of_evenly_divisible(nums):
    for combination in combinations(nums, 2):
        if max(combination) % min(combination) == 0:
            return max(combination) // min(combination)

def test_conversion():
    spreadsheet_file = "5 1 9 5\n" \
                       "7 5 3\n" \
                       "2 4 6 8"
    
    gen = convert_to_ints(spreadsheet_file.split('\n'))
    assert next(gen) == [5,1,9,5]
    assert next(gen) == [7,5,3]
    assert next(gen) == [2,4,6,8]

def test_diff_of_min_and_max():
    assert diff_of_min_and_max([5,1,9,5]) == 8

def test_div_of_evenly_divisible():
    assert div_of_evenly_divisible([5,9,2,8]) == 4

def test_pt1():
    spreadsheet = [[5,1,9,5], [7,5,3], [2,4,6,8]]
    assert calc_checksum(spreadsheet, diff_of_min_and_max) == 18

def test_pt2():
    spreadsheet = [[5,9,2,8], [9,4,7,3], [3,8,6,2]]
    assert calc_checksum(spreadsheet, div_of_evenly_divisible) == 9
    
if __name__ == '__main__':
    with open('input', 'r') as f:
        spreadsheet = list(convert_to_ints(f))
        print(f"Result part1: { calc_checksum(spreadsheet, diff_of_min_and_max) }")
        print(f"Result part2: { calc_checksum(spreadsheet, div_of_evenly_divisible) }")

