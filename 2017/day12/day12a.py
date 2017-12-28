#!/usr/local/bin/python3
from collections import deque

def parse(line):
    """
    >>> parse('2 <-> 0, 3, 4')
    (2, [0, 3, 4])
    """
    pid, children = line.split(' <-> ')
    pid = int(pid)
    children = { int(child) for child in children.split(',') }
    return pid, children 

def solve(fp):
    visited = set()
    work = { 0 }
    programs = [line for line in fp]

    while work:
        pid = work.pop()

        _, children = parse(programs[pid])

        visited.add(pid)
        work.update(children - visited)

    return len(visited)

def main():
    import sys
    print(f'Part 1: { solve(sys.stdin) }')

if __name__ == '__main__':
    main()
