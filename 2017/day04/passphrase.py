from itertools import combinations
from collections import Counter

def equality_policy(passphrase):
    """ Tests if words in passphrase only occur once
    
    :passphrase: Space separated passphrase 
    :returns: True if all parts only occur once 

    >>> equality_policy('aa bb cc dd ee')
    True
    >>> equality_policy('aa bb cc dd aa')
    False
    >>> equality_policy('aa bb cc dd aaa')
    True
    """
    words = passphrase.split()
    unique_words = set(words)
    return len(words) == len(unique_words)

def is_anagram(w1, w2):
    """ Test if two words are an anagram

    :w1: word
    :w2: word
    :returns: True if words are anagrams of eachother

    >>> is_anagram('oiii', 'ioii')
    True
    >>> is_anagram('oiii', 'ooii')
    False
    """
    # Anagrams must have the same length
    if len(w1) != len(w2):
        return False

    # Test if anagram by comparing the counts of the letters.
    # First create a dictionary of letter counts for the first word.
    # Then subtract the letter counts from that dictionary.
    letter_count = Counter(w1)
    for letter in w2:
        try:
            letter_count[letter] -= 1
        except:
            return False

    return all(value == 0 for key, value in letter_count.items())

def anagram_policy(passphrase):
    """ Tests if passphrase does not contain anagrams

    :passphrase: Words of a passphrase separated by spaces
    :returns: True if passphrase does not contain anagrams

    >>> anagram_policy('abcde fghij')
    True
    >>> anagram_policy('abcde xyz ecdab')
    False
    >>> anagram_policy('a ab abc abd abf abj')
    True
    >>> anagram_policy('iiii oiii ooii oooi oooo')
    True
    >>> anagram_policy('oiii ioii iioi iiio')
    False
    """
    words = passphrase.split()
    return not any(is_anagram(w1, w2) for w1,w2 in combinations(words, 2))

def solve(passphrases, policy_func):
    """ Counts number of valid passphrases given a policy function

    :passphrases: Collection of passphrases
    :returns: Number of valid passphrases

    >>> solve(['a b c', 'b c d', 'aa bb cc'], equality_policy)
    3
    >>> solve(['a b c', 'b c d', 'abc cba'], anagram_policy)
    2
    """
    n = 0
    for passphrase in passphrases:
        if policy_func(passphrase):
            n += 1
    return n

def main():
    with open('input.txt', 'r') as f:
        f = list(f)
        print(f'Part 1: {solve(f, equality_policy)}')
        print(f'Part 2: {solve(f, anagram_policy)}')

if __name__ == '__main__':
    main()
