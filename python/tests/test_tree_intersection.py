from code_challenges.tree_intersection.tree_intersection import *

def test_tree_insertion():
    expected = [5, 3, 6]
    tree1 = BinaryTree()
    tree1.add(5)
    tree1.add(3)
    tree1.add(2)
    tree1.add(6)
    tree2 = BinaryTree()
    tree2.add(5)
    tree2.add(1)
    tree2.add(3)
    tree2.add(6)
    actual =tree_intersection(tree1, tree2)
    assert actual == expected

def test_no_intersection():
    expected = "there is no intersection between these trees"
    tree1 = BinaryTree()
    tree1.add(5)
    tree1.add(3)
    tree1.add(2)
    tree1.add(6)
    tree2 = BinaryTree()
    tree2.add(4)
    tree2.add(1)
    tree2.add(8)
    tree2.add(9)
    actual =tree_intersection(tree1, tree2)
    assert actual == expected

def test_empty_trees():
        expected = "trees are empty!"
        tree1 = BinaryTree()
        tree2 = BinaryTree()
        actual = tree_intersection(tree1, tree2)
        assert actual == expected

def test_second_tree_empty():
        expected = "Only one tree can be found"
        tree1 = BinaryTree()
        tree1.add(5)
        tree1.add(3)
        tree1.add(2)
        tree1.add(6)
        tree2 = BinaryTree()
        actual = tree_intersection(tree1, tree2)
        assert actual == expected


