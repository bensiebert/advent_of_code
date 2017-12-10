def offset_func_pt1(*args):
    return 1 

def offset_func_pt2(offset):
    if offset >= 3:
        return -1
    else:
        return 1 

def escape(maze, offset_func):
    """
    >>> escape([0,3,0,1,-3], offset_func_pt1)
    5
    >>> escape([0,3,0,1,-3], offset_func_pt2)
    10
    """
    pointer = 0
    steps = 0
    maze_size = len(maze)
    while pointer < maze_size:
        offset = maze[pointer]
        maze[pointer] += offset_func(offset)
        pointer += offset
        steps += 1
    return steps 

def main():
    with open('input.txt', 'r') as f:
        maze = [int(offset) for offset in f]
        print(f'Part1: { escape(maze, offset_func_pt1) }')
    with open('input.txt', 'r') as f:
        maze = [int(offset) for offset in f]
        print(f'Part2: { escape(maze, offset_func_pt2) }')

if __name__ == '__main__':
    main()
