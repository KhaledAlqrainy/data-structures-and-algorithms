from Data_Structure.trees import *

def fizz_buzz_tree(Ktree):

    tree = BinaryTree()
    if not Ktree.root: 
        return tree

    def walk(current):
        node = Node(matching(current.data))

        if current.left: 
            node.left = walk(current.left)
        
        if current.right: 
            node.right = walk(current.right)
        return node

    tree.root = walk(Ktree.root)
    return tree

def matching(num):

    if num % 3 == 0 and num % 5 == 0: 
        return "FizzBuzz"
    
    elif num % 3 == 0: 
        return "Fizz"
    
    elif num % 5 == 0: 
        return "Buzz"
    
    elif num % 3 != 0 and num % 5 != 0: 
        return num
    
    else: 
        return str(num)

