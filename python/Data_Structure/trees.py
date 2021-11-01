"""
This Module defines a Node and a Binary Tree
"""

class Node:
  def __init__ (self,data,left=None,right=None):
    self.data = data
    self.left = left
    self.right = right

class Queue:
  def __init__(self, collection=[]):
    self.data = collection

  def peek(self):
    if len(self.data):
      return True
    return False
    
  def enqueue(self,item):
    self.data.append(item)
    
  def dequeue(self):
    return self.data.pop(0)

class BinaryTree:
  
  def _init_(self):
    self.root = None

  def bfs(self):
    """
    A binary tree method which returns a list of items that it contains

    input: None

    output: tree items
    """
    breadth = Queue()
    breadth.enqueue(self.root)

    list_of_items = []

    while breadth.peek():
      front = breadth.dequeue()
      list_of_items += [front.data]

      if front.left:
        breadth.enqueue(front.left)

      if front.right:
        breadth.enqueue(front.right)

    return list_of_items

  def pre_order(self):
    """
    A binary tree method which returns a list of items that it contains

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

  def in_order(self):
    """
    function to in order the list using Trees
    """
    list_of_items = []
    def walk(node):
      if node:
        if node.left:
          walk(node.left)
        list_of_items.append(node.data)
        if node.right:
          walk(node.right)

    walk(self.root)
    return list_of_items

  def post_order(self):
    """
    A binary tree method which returns a list of items in post order 

    input: None

    output: tree items
    """
    list_of_items = []
    def walk(node):
      if node:
        if node.left:
          walk(node.left)
        if node.right:
          walk(node.right)
        list_of_items.append(node.data)    

    walk(self.root)
    return list_of_items


  def max(self):
    """
    A function that takes a values in tree and return the maximum value in that tree.
    
    """
    self.data =0 

    def walk(current):

      if current:

        if current.data > self.data:
          self.data = current.data
        
        if current.right:
          walk(current.right)
        
        if current.left:
          walk(current.left)

    walk(self.root)
    return self.data

  def breadth_first(self, tree):

    """
    A function that Return list of all values in the tree, in the order they were encountered

    """

    if tree.root is None:
      return 'Tree is Empty'

    temp = []
    results = []
    
    if self.root:
        temp.append(self.root)
        
        while temp:
          node = temp.pop(0)
          results.append(node.data)
          
          if node.left:
              temp.append(node.left)
          if node.right:
              temp.append(node.right)
        return results

  
        


  

  