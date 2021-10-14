class Node:
  """
  A class representing a Node

  Attributes
  ----------


  Methods
  -------
  __init__(data, next_):
      the constructor method for the class, it takes two parameters, the data parameter is the a reference to the data the node will hold, and the next_ 

  """

  def __init__(self, data, next_ = None):
    self.data = data
    self.next_ = next_

    

    

class LinkedList:
  """
  A class for creating instances of a Linked List.
  
  Data and other attributes defined here:
  
  head: Node | None

  Methods defined here

  insert(value: any)
  contains(value: any) -> bool
  """

  def __init__(self):
    self.head = None

    """"
    Insert creates a Node with the value that was passed and adds
    it to the head of the linked list shifting all other values down

    arguments:
    value : any

    returns: None
    """
  
    def insert (self, data):
        new_node = Node (data, self.head)
        self.head = new_node
        self.size += 1

    def includes (self, data):
        this_node = self.head
        while this_node:
            if this_node.get_data() == data:
                return True
            else:
                this_node = this_node.get_next()
        return False


    def __str__(self):
        if self.head:
            saved_data = "{"f"{self.head.data}""} "
            this_node = self.head
            while this_node:
                this_node = this_node.next_node
                if  this_node:
                    saved_data += "-> ""{"f"{ this_node.data}""} "
                else:
                    saved_data += "-> NULL"
        else:
            return "Your List still empty"
        return saved_data


myList = LinkedList()
print(myList.includes(5))
print(myList.includes(3))
print(myList.__str__())