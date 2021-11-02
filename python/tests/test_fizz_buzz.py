from code_challenges.tree_fizz_buzz import *

def test_fizz_buzz():
    fizz = BinaryTree()
    fizz.root = Node(1)
    fizz.root.left = Node(10)
    fizz.root.right = Node(12)
    fizz.root.left.left = Node(2)
    fizz.root.left.right = Node(18)
    fizz.root.right.right = Node(15)
    actual = fizz_buzz_tree(fizz).pre_order()
    print(actual)
    expected = "[1, 'Buzz', 2, 'Fizz', 'Fizz', 'FizzBuzz']"
    assert actual == expected

def test_fizz_buzz_second():
    fizz = BinaryTree()
    fizz.root = Node(1)
    fizz.root.left = Node(3)
    fizz.root.right = Node(9)
    fizz.root.left.left = Node(12)
    fizz.root.left.right = Node(15)
    fizz.root.right.right = Node(18)
    fizz.root.right.right.right = Node(30)
    actual = fizz_buzz_tree(fizz).pre_order()
    print(actual)
    expected = "[1, 'Fizz', 'Fizz', 'FizzBuzz', 'Fizz', 'Fizz', 'FizzBuzz']"
    assert actual == expected