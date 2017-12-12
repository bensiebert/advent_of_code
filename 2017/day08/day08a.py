#!/usr/local/bin/python3
from collections import defaultdict
import sys

registers = defaultdict(int)
for line in sys.stdin:
    words = line.split()
    register = words[0]    
    func = words[1]
    amount = int(words[2])
    cmp_register = words[4]
    cmp_func = words[5]
    cmp_amount = int(words[6])
    if eval(f"registers['{cmp_register}'] {cmp_func} {cmp_amount}"):
        if func == 'inc':
            registers[register] += amount
        else:
            registers[register] -= amount

print(max(registers.values()))
