import pytest
from captcha_solver import solve

def test_empty_list():
    assert solve('') == 0

def test_single_item_list():
    assert solve('5') == 5

def test_simple():
    assert solve('1122') == 3

def test_all_equal_digits():
    assert solve('1111') == 4

def test_no_equal_digits():
    assert solve('1234') == 0

def test_only_circular_match():
    assert solve('91212129') == 9

def test_works_with_ints():
    assert solve(91212129) == 9

def test_hand():
    assert solve(3312349912343) == 3+9+3

def test_halfway():
    input_num = '1212'
    assert solve(input_num, look_ahead = len(input_num)//2) == 6
    input_num = '1221'
    assert solve(input_num, look_ahead = len(input_num)//2) == 0
    input_num = '123425'
    assert solve(input_num, look_ahead = len(input_num)//2) == 4
    input_num = '123123'
    assert solve(input_num, look_ahead = len(input_num)//2) == 12
    input_num = '12131415'
    assert solve(input_num, look_ahead = len(input_num)//2) == 4
