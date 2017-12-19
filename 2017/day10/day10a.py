#!/usr/local/bin/python3
import sys

def rotate(nums, pos, length):
    """
    >>> nums = [0,1,2,3,4,5]
    >>> rotate(nums, 4, 3)
    >>> nums
    [4, 1, 2, 3, 0, 5]
    >>> nums = [0,1,2,3,4]
    >>> rotate(nums, 0, 3)
    >>> nums
    [2, 1, 0, 3, 4]
    """
    nums_size = len(nums)
    for n in range(length // 2):
        pos_a = (pos + n) % nums_size
        a = nums[pos_a]

        pos_b = (pos + length - 1 - n) % nums_size
        b = nums[pos_b]
        
        nums[pos_a] = b
        nums[pos_b] = a

def solve(nums, lengths):
    """
    >>> nums = [0,1,2,3,4]
    >>> lengths = [3,4,1,5]
    >>> solve(nums, lengths)
    [3, 4, 2, 1, 0]
    """
    pos = 0
    skip_size = 0 
    for length in lengths:
        rotate(nums, pos, length)
        pos += length + skip_size
        skip_size += 1
    return nums

def main():
    nums = list(range(256))
    lengths = [int(length) for length in sys.stdin.read().split(',')]
    solve(nums, lengths)
    print(f'Part1: { nums[0]*nums[1] }')

if __name__ == '__main__':
    main() 
