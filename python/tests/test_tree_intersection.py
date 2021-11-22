from code_challenges.tree_intersection.tree_intersection import *

def test_tree_intersection():

    tree = BinaryTree(55)
    tree.root.left = Node(7)
    tree.root.left.left = Node(15)
    tree.root.left.right = Node(88)
    tree.root.left.right.left = Node(9)
    tree.root.left.right.right = Node(11)
    tree.root.right = Node(14)
    tree.root.right.left= Node(22)
    tree.root.right.right = Node(3)
    tree.root.right.right.left = Node(4)
    tree.root.right.right.right = Node(77)

    tree1 = BinaryTree(26)
    tree1.root.left = Node(7)
    tree1.root.left.left = Node(75)
    tree1.root.left.right = Node(15)
    tree1.root.left.right.left = Node(9)
    tree1.root.left.right.right = Node(11)
    tree1.root.right = Node(18)
    tree1.root.right.left= Node(22)
    tree1.root.right.right = Node(3)
    tree1.root.right.right.left = Node(33)
    tree1.root.right.right.right = Node(77)

    expected = [7, 15, 9, 11, 22, 3, 77]
    actual = tree_intersection(tree, tree1)
    assert actual == expected