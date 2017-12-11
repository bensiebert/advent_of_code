#!/usr/local/bin/python3
import re

class Program:
    def __init__(self, name, weight, parent=None, children=[]):
        self.name = name
        self.weight = weight
        self.parent = parent
        self.children = children
        
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

    return Program(name, weight, parent=None, children=children)

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

def main():
    with open('input.txt', 'r') as f:
        solve(f)

if __name__ == '__main__':
    main()
