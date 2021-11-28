"""
The implementation of Node class, Linked list class, and Hashmap class. 
"""


class Node:
    def __init__(self, key, value):

      self.key = key
      self.value = value
      self.next = None


class LinkedList:
    def __init__(self):
        """
        The constructor method for the linked list. Initializes the head of a linked list to None.
        """
        self.head = None

    def insert(self,key ,value):
        """
        Take a value and store it in a Node, then insert it to the beginning of the linked list.
        """
        self.head = Node(key,value)


class HashTable:

    def __init__(self, size=1024):
        """
        Initalization of Hash table
        
        """
        self.size = size
        self.__buckets = [None] * size

    def __hash(self, key):
        """
        Takes a key which is a string and returns an integer which is the index that will be used to store the key/value pari in a Node at that index.
        """
        total = 0

        for i in key:
            total += ord(i)
        hash_key = (total*7)%(self.size)

        return hash_key

    def add(self, key, value):
        """
        A method for adding a new value to the map
        This method should hash the key, and add the key and value pair to the table.

        Arg: Takes the key and value 
        Return : No return value
        """

        index = self.__hash(key)

        if not self.__buckets[index]:
          self.__buckets[index] = LinkedList()
          self.__buckets[index].insert(key,value)

        else:
          self.__buckets[index].insert(key,value)

    def get(self, key):
      """
      Retrieve the most recent value of in our hasmap for the given key

      :param key str
      :value any
      """
      # calculate index
      index = self.__hash(key)
      # check if there is a non empty bucket at the index
      if self.__buckets[index]:
        # iterate over linked list
        linked_list = self.__buckets[index]
        current = linked_list.head
        while current:
          # check if the key in each node matches
          if current.key == key: 
            # return the value of the node with the mathcing key
            return current.value
          current = current.next
      return None
        
      # # return None
      # return None

    def contains(self,key):

        index = self.__hash(key)
        if self.__buckets[index]:

            current = self.__buckets[index].head
            while current:
                if current.key == key:
                    return True
                current = current.next
        else:
            return False

if __name__ == "__main__":
    hashtable = HashTable()
    hashtable.add("yahya", 10)
    hashtable.add("go", 'play football')
    hashtable.add("no", False)
    print(hashtable.get("go"))
    print(hashtable.get("no"))
    print(hashtable.contains("yahya"))
    print(hashtable.hash('united'), "hashh")

# if __name__ == "__main__":
#     hashtable = HashTable()
#     hashtable.add("Khaled", 10)
#     hashtable.add("Forza", 'Milan')
#     hashtable.add("no", False)
#     print(hashtable.get("Forza"))
#     print(hashtable.get("no"))
#     print(hashtable.contains("Khaled"))
#     print(hashtable.__hash('united'), "hashh")
      
        