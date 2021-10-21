class Node:

  def __init__(self, data=None):
    self.data = data
    self.next = None

########## Stack ###########

class Stack:

  def __init__(self, node=None):
    self.top = node

  def push(self, data):
    if not self.top:
      self.top = Node(data)

    else:
      node = Node(data)
      node.next = self.top
      self.top = node

  def pop(self):

    if not self.is_empty():
      item = self.top
      self.top = self.top.next
      item.next = None
      return item.data
    else:
        return 'Stack is Empty'

  def peek(self):

    if not self.is_empty():
      return self.top.data

    return "Stack is Empty"

  def is_empty(self):

    if self.top:
      return False

    return True

  def __str__(self):
      
    item = self.top
    list = []

    while item:
      list.append(str(item.data))
      item = item.next
    return "\n".join(list)

############ QUEUE ##############

class Queue:
    
    def __init__(self):
        self.front = None
        self.empt = None

    def enqueue(self, data):

        node = Node(data)

        if not self.front:
            self.front = node
            self.empt = node
        else:
            self.empt.next = node
            self.empt = self.empt.next

    def dequeue(self):

        item = self.front
        self.front = self.front.next
        item.next = None
        return item.data

    def peek(self):

        if not self.is_empty():
            return self.front.data
        else:
           return "Queue is Empty"

    def is_empty(self):

        if self.front:
            return False
        else:
            return True

    def __str__(self):

        item = self.front
        list = []
        while item:
            list.append(str(item.data))
            item = item.next
        return "\n".join(list)

    

