#!/usr/local/bin/python3
# Solution too much inspired by: https://github.com/mcbor/adventofcode/blob/master/2017/07b.py
import re

class Program:
    def __init__(self, name, weight, parent=None, children=[]):
        self.name = name
        self.weight = weight
        self.parent = parent
        self.children = children
     
    def total_weight(self):
        return self.weight + sum(child.total_weight() for child in self.children)
    
    def is_balanced(self):
        return len(set(child.total_weight() for child in self.children)) == 1

        
PROGRAM_REGEX = re.compile(r'^(?P<name>.+?) \((?P<weight>.+?)\)( -> (?P<children>.+?))?$')
def parse(program_str):
    """
    >>> in_prog = 'vmreal (6560) -> fpqpaes, fjxvx, nyrjj'
    >>> program = parse(in_prog)
    >>> program.name
    'vmreal'
    >>> program.weight
    6560
    >>> program.children
    ['fpqpaes', 'fjxvx', 'nyrjj']
    """
    result = PROGRAM_REGEX.match(program_str)    

    name = result.group('name')
    weight = int(result.group('weight'))
    children = []

    raw_children = result.group('children') 
    if raw_children:
        children = raw_children.split(', ')

    return Program(name, weight, children=children)

def transform_to_tree(raw_programs):
    for name, program in raw_programs.items():
        program.children = [raw_programs[child] for child in program.children] 

        for child in program.children:
            child.parent = program

def find_bottom(programs):
    program = next(iter(programs.values()))

    while program.parent:
        program = program.parent

    return program

def solve(tower_file):
    programs = {}
    for program_str in tower_file:
        raw_program = parse(program_str)
        programs[raw_program.name] = raw_program
    
    transform_to_tree(programs)
    bottom_program = find_bottom(programs)
    print(f"Part 1: { bottom_program.name }")

    program = bottom_program
    while True:
        for child in program.children:
            if not child.is_balanced():
                program = child
                break
        else:
            weights = [child.total_weight() for child in program.children]
            idx, = [i for i, w in enumerate(weights) if weights.count(w) == 1]
            offbalance = program.children[idx]
            diff = weights[idx] - weights[not idx]
            
            print(f"{ offbalance.weight - diff }")

        
            #print(f'{ child.total_weight() }')

    #print(f"Part 2: { bottom_program.total_weight() }")

def main():
    with open('input.txt', 'r') as f:
        solve(f)

if __name__ == '__main__':
    main()
