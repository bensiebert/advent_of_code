#!/usr/local/bin/python3

def find_target(mem_banks):
    """
    >>> find_target([1,2,5,3,5])
    2
    >>> find_target([1,1,1,1,1])
    0
    >>> find_target([5,4,3,2,1])
    0
    >>> find_target([1,2,3,4,5])
    4
    """
    largest_bank = 0
    most_blocks = 0
    for idx, blocks in enumerate(mem_banks):
        if blocks > most_blocks:
            most_blocks = blocks
            largest_bank = idx
    return largest_bank

def reallocate(mem_banks, target):
    """
    >>> mem_banks = [0,2,7,0]
    >>> reallocate(mem_banks, 2)
    >>> mem_banks
    [2, 4, 1, 2]
    """
    blocks = mem_banks[target]
    mem_banks[target] = 0
    num_of_banks = len(mem_banks)
    pointer = (target + 1) % num_of_banks 
    while blocks > 0:
        mem_banks[pointer] += 1
        blocks -= 1
        pointer = (pointer + 1) % num_of_banks

def solve(mem_banks):
    """
    >>> solve([0,2,7,0])
    (5, 4)
    """
    past_layouts = []
    realloc_cnt = 0
    while mem_banks not in past_layouts:
        past_layouts.append(mem_banks[:])
        target = find_target(mem_banks)
        reallocate(mem_banks, target)
        realloc_cnt += 1

    cycle_start_idx = past_layouts.index(mem_banks)
    cycle_length = realloc_cnt - cycle_start_idx

    return realloc_cnt, cycle_length

def main():
    with open('input.txt', 'r') as f:
        mem_banks = [int(bank) for bank in f.read().split()]
        reallocations, cycle_length = solve(mem_banks) 
        print(f"Part 1: { reallocations }")
        print(f"Part 2: { cycle_length }")

if __name__ == '__main__':
    main()
