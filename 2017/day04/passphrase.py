def valid(passphrase):
    """ Validates a passphrase if its parts only occur once
    
    :passphrase: Space separated passphrase 
    :returns: True if all parts only occur once 

    >>> valid('aa bb cc dd ee')
    True
    >>> valid('aa bb cc dd aa')
    False
    >>> valid('aa bb cc dd aaa')
    True
    """
    words = passphrase.split()
    unique_words = set(words)
    return len(words) == len(unique_words)

def solve(passphrases):
    """ Counts number of valid passphrases

    :passphrases: Collection of passphrases
    :returns: Number of valid passphrases

    >>> solve(['a b c', 'b c d', 'aa bb cc'])
    3
    """
    n = 0
    for passphrase in passphrases:
        if valid(passphrase):
            n += 1
    return n

def main():
    with open('input.txt', 'r') as f:
        print(f'Part 1: {solve(f)}')

if __name__ == '__main__':
    main()
