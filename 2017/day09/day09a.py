#!/usr/local/bin/python3
def calc_score(text):
    """
    >>> calc_score('{}')
    1
    >>> calc_score('{{{}}}')
    6
    >>> calc_score('{{},{}},')
    5
    >>> calc_score('{{{},{},{{}}}}')
    16
    >>> calc_score('{<a>,<a>,<a>,<a>}')
    1
    >>> calc_score('{{<ab>},{<ab>},{<ab>},{<ab>}}')
    9
    >>> calc_score('{{<!!>},{<!!>},{<!!>},{<!!>}}')
    9
    >>> calc_score('{{<a!>},{<a!>},{<a!>},{<ab>}}')
    3
    """
    ignore = False
    depth = 0
    garbage = False
    score = 0

    for c in text:
        if ignore:
            ignore = False
            continue

        if c == '!':
            ignore = True
            continue

        if c == '>':
            garbage = False
            continue

        if garbage:
            continue

        if c == '<':
            garbage = True
            continue

        if c == '{':
            depth += 1
            score += depth
            continue

        if c == "}":
            depth -= 1
            continue
    
    return score

def solve(text):
    return calc_score(text)

def main():
    import sys
    print(calc_score(sys.stdin.read()))

if __name__ == '__main__':
    main()
