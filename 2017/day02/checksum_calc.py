import pytest

def convert_to_ints(file_input):
    for line in file_input:
        yield [int(num) for num in line.split()]

def calc_checksum(spreadsheet):
    checksum = 0

    for line in spreadsheet:
        difference = max(line) - min(line)
        checksum += difference

    return checksum

def test_conversion():
    spreadsheet_file = "5 1 9 5\n" \
                       "7 5 3\n" \
                       "2 4 6 8"
    
    gen = convert_to_ints(spreadsheet_file.split('\n'))
    assert next(gen) == [5,1,9,5]
    assert next(gen) == [7,5,3]
    assert next(gen) == [2,4,6,8]

def test_calc_checksum():
    spreadsheet = [[5,1,9,5], [7,5,3], [2,4,6,8]]
    assert calc_checksum(spreadsheet) == 18
    
if __name__ == '__main__':
    import sys
    with open('input', 'r') as f:
        spreadsheet = convert_to_ints(f)
        checksum = calc_checksum(spreadsheet)
    print(checksum)

