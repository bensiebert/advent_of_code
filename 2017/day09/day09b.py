#!/usr/local/bin/python3
def calc_garbage(text):
    """
    >>> calc_garbage('<>')
    0
    >>> calc_garbage('<random characters>')
    17
    >>> calc_garbage('<<<<>')
    3
    >>> calc_garbage('<{!>}>')
    2
    >>> calc_garbage('<!!>')
    0
    >>> calc_garbage('<!!!>>')
    0
    >>> calc_garbage('<{o"i!a,<{i<a>')
    10
    """
    ignore = False
    garbage_mode = False

    garbage = ''

    for c in text:
        if ignore:
            ignore = False
            continue

        if c == '!':
            ignore = True
            continue

        if c == '>':
            garbage_mode = False
            continue

        if garbage_mode:
            garbage += c
            continue

        if c == '<':
            garbage_mode = True
            continue

        if c == '{':
            continue

        if c == "}":
            continue
    
    return len(garbage)

def solve(text):
    return calc_garbage(text)

def main():
    import sys
    print(solve(sys.stdin.read().strip()))

if __name__ == '__main__':
    main()
