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

def get_group(programs, pid):
    visited = set()
    work = { pid }

    while work:
        pid = work.pop()

        _, children = parse(programs[pid])

        visited.add(pid)
        work.update(children - visited)

    return visited
    

def solve(fp):
    programs = [line for line in fp]
    pids = set(range(len(programs)))
    groups = 0

    while pids:
        pid = pids.pop()
        group = get_group(programs, pid)
        pids -= group
        groups += 1

    return groups

def main():
    import sys
    print(f'Part 2: { solve(sys.stdin) }')

if __name__ == '__main__':
    main()
