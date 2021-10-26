from code_challenges.stack_queue_brackets import *


def test_1():
    first = validate_brackets('{}')
    actual = first
    assert actual == first

def test_2():
    second = validate_brackets('{}(){}')
    actual = second
    assert actual == second

def test_3():
    third = validate_brackets('()[[Extra Characters]]')
    actual = third
    assert actual == third

def test_4():
    fourth = validate_brackets('(){}[[]]')
    actual = fourth
    assert actual == fourth

def test_5():
    fifth = validate_brackets('{}{Code}[Khaled](())')
    actual = fifth
    assert actual == fifth

