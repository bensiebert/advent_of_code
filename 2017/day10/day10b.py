#!/usr/local/bin/python3
import sys
from operator import xor
from functools import reduce

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

def solve(nums, in_str):
    """
    >>> solve(list(range(256)), '')
    'a2582a3a0e66e6e86e3812dcb672a272'
    >>> solve(list(range(256)), 'AoC 2017')
    '33efeb34ea91902bb2f59c9920caa6cd'
    >>> solve(list(range(256)), '1,2,3')
    '3efbe78a8d82f29979031a4aa0b16a9d'
    >>> solve(list(range(256)), '1,2,4')
    '63960835bcdc130f0b66d7ff4f6a5a8e'
    """
    inp = prepare_input(in_str)
    to_sparse(nums, inp)
    dense = to_dense(nums)
    return to_hex(dense)

def to_ascii(in_str):
    """
    >>> list(to_ascii('1,2,3'))
    [49, 44, 50, 44, 51]
    """
    return (ord(c) for c in in_str)

def prepare_input(in_str):
    """
    >>> prepare_input('1,2,3')
    [49, 44, 50, 44, 51, 17, 31, 73, 47, 23]
    """
    as_ascii = list(to_ascii(in_str))
    as_ascii += [17, 31, 73, 47, 23]
    return as_ascii

def to_sparse(nums, lengths):
    pos = 0
    skip_size = 0 
    for _ in range(64):
        for length in lengths:
            rotate(nums, pos, length)
            pos += length + skip_size
            skip_size += 1

def to_dense(sparse):
    """
    >>> reduce(xor, [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22])
    64
    """
    for i in range(0, 256, 16):
        sliced = sparse[i:i+16]
        yield reduce(xor, sliced)

def to_hex(nums):
    """
    >>> to_hex([64, 7, 255])
    '4007ff'
    """
    hex_nums = (hex(num)[2:] for num in nums)
    hex_nums = (num.zfill(2) for num in hex_nums)
    return "".join(hex_nums)

def main():
    nums = list(range(256))
    lengths = sys.stdin.read().strip()
    print(f'Part 2: { solve(nums, lengths) }')

if __name__ == '__main__':
    main() 
