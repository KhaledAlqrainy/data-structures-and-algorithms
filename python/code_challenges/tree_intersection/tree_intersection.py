from Data_Structure.hashTable.hashmap import HashTable

class Node:
  def __init__ (self,data,left=None,right=None):
    self.data = data
    self.left = left
    self.right = right

class BinaryTree:

    def __init__(self):
        self.root = None

    def pre_order(self):
        """
        A binary tree method which returns a list of items that it contains in pre_order
        input: None
        output: tree items
        sub method : walk () to make the recursion staff
        """
        list_of_items = []
        def walk(node):
            if node:
                list_of_items.append(node.data)
                if node.left:
                    walk(node.left)
                if node.right:
                    walk(node.right)

        walk(self.root)
        return list_of_items

    def add(self,value):

        if not self.root:
            self.root= Node(value)
        else :
            temp = self.root
            while temp:
                if value < temp.data:
                    if not temp.left:
                        temp.left = Node(value)
                        break
                    temp = temp.left
                else:
                    if not temp.right:
                        temp.right = Node(value)
                        break
                    temp = temp.right


def tree_intersection(first_tree , second_tree):

    tree1 = first_tree.pre_order()
    tree2 = second_tree.pre_order()

    if not tree1 and not tree2:
        return "trees are empty!"
    if not tree1 or not tree2:
        return "Only one tree can be found"

    values =[]
    hash_table = HashTable()
    for node in tree1:
        hash_table.add(str(node),node)

    for node in tree2:
        if hash_table.contains(str(node)):
            values.append(node)
        else :
            hash_table.add(str(node),node)

    if not values:
        return "there is no intersection between these trees"
    return values
