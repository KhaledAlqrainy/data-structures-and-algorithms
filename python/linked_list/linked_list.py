
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
  
  def insert(self, data):
        """
        insert a node in the list

        """
        new_node = Node(data,self.head)
        # new_node.next_=self.head
        self.head=new_node

  def includes(self, data):
        """
        check if the value exist in the list
        return a boolean: True if exist, False if not

        """
        if self.head is None:
            return False
        else:
            item=self.head
            while(item):
                if(item.data==data):
                    return True

                item=item.next_

            return False 
                    
  def to_string(self):

        """
        return a string of the list

        """

        item=self.head
        space=''
        if item !=None:
                while(item):
                    space+='{'+str(item.data)+'}->'
                    item=item.next_
                return space+'NULL'

  def append(self,data):

        """
        A function to add a node in the end of list
        """
        newValue=Node(data)
        
        if self.head is None:
            self.head = newValue
        else:

            last= self.head

            while (last.next_):
                last = last.next_
            last.next_ = newValue

  def insert_before(self,data, newValue):

        """
        A function that adds a new node with the given new value immediately before the first node that has the value specified
        """

        if self.head is None:
            return 'Linked List is Empty'
            
        newValue1=Node(newValue)
        last=self.head

        while(last.next_):
            if last.next_.data==data:
                newValue1.next_=last.next_
                last.next_=newValue1
                return
                 

  def insert_after(self,value, newValue):

        """
        A function that adds a new node with the given new value immediately after the first node that has the value specified
        """
        
        last=self.head

        while last:
            if last.data == value:
                newValue = last.next_
                last.next_ = Node(newValue)
                last.next_.next_ = newValue
                break
            last = last.next_
            return
            

        
        
    

            
                
             



    

