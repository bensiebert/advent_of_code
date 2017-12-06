from enum import Enum

class Direction(Enum):
    DOWN = (0,1)
    RIGHT = (1,0)
    UP = (0,-1)
    LEFT = (-1,0)

turn_left = {
    Direction.DOWN: Direction.RIGHT,
    Direction.RIGHT: Direction.UP,
    Direction.UP: Direction.LEFT,
    Direction.LEFT: Direction.DOWN
}

def add_pos(pos, delta):
    """
    Adds two (x,y) tuples, (x1+x2, y1+2).
    """
    x, y = pos
    dx, dy = delta
    return (x+dx, y+dy)

def new_position_direction(matrix, position, direction):
    """
    determines new position and direction
    turn left if you can, else move forward
    """
    left_direction = turn_left[direction]
    left_pos = add_pos(position, left_direction.value)
    if left_pos not in matrix:
        return left_pos, left_direction
    else:
        forward_pos = add_pos(position, direction.value)
        return forward_pos, direction

def gen_matrix():
    """
    Yields each position coords and step number
    """
    matrix = {}
    position = (0,0)
    direction = Direction.DOWN
    step = 1

    while True:
        yield position, step

        matrix[position] = step
        step += 1

        position, direction = new_position_direction(matrix, position, direction)

def gen_matrix2():
    """
    Yields the spiral's value of each step
    """
    matrix = {}
    position = (0,0)
    direction = Direction.DOWN

    deltas = [
        (-1,-1),( 0,-1),( 1,-1),
        (-1, 0)        ,( 1, 0),
        (-1, 1),( 0, 1),( 1, 1)
    ]

    insert_value = 1
    while True:
        yield insert_value
        matrix[position] = insert_value

        position, direction = new_position_direction(matrix, position, direction)

        insert_value = 0
        for delta in deltas:
            lookup_pos = add_pos(position, delta)
            try:
                insert_value += matrix[lookup_pos]
            except:
                pass

def solve_part1():
    g = gen_matrix()
    position = (0,0)
    while True:
        position, step = next(g)
        if step == 265149:
            x,y = position
            return abs(x) + abs(y)

def solve_part2():
    g = gen_matrix2()
    while True:
        val = next(g)
        if val > 265149:
            return val

if __name__ == '__main__':
    print(f"Part 1: { solve_part1() }")
    print(f"Part 2: { solve_part2() }")
