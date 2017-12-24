#!/usr/local/bin/python3
class Hex:
    """
    >>> h1 = Hex(0,0,0)
    >>> h2 = Hex(-2,2,0)
    >>> h2.distance(h1)
    2
    """
    def __init__(self, x, y, z):
        assert x + y + z == 0
        self._x = x
        self._y = y
        self._z = z

    def __add__(self, other):
        x = self._x + other._x
        y = self._y + other._y
        z = self._z + other._z
        return Hex(x, y, z) 

    def distance(self, other):
        dx = abs(self._x - other._x)
        dy = abs(self._y - other._y)
        dz = abs(self._z - other._z)
        return (dx + dy + dz) // 2

DIRECTIONS = {
    'nw': Hex(-1, 1, 0),
    'n':  Hex(0, 1, -1),
    'ne': Hex(1, 0, -1),
    'se': Hex(1, -1, 0),
    's':  Hex(0, -1, 1),
    'sw': Hex(-1, 0, 1),
}

def solve(directions):
    distances = []
    origin = Hex(0,0,0)
    loc = Hex(0,0,0)
    for direction in directions.split(','):
        loc += DIRECTIONS[direction]
        distances.append(loc.distance(origin))
    return max(distances)

def main():
    import sys
    directions = sys.stdin.read().strip()
    print(f'Part 2: { solve(directions) }')

if __name__ == '__main__':
    main()
