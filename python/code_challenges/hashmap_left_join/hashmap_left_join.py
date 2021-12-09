class HashTable():
  def __init__(self ,size = 1024):
    """initialization hash table"""
    self.max = size 
    self.arr = [[] for i in range(self.max)] 
    

  def get_hash(self, key):
    """function to return the hash value using ASCII code"""
    h = 0
    for char in key:
        h += ord(char)
    hash_index= h % self.max 
    return hash_index
 
  def add(self ,key ,value):
    """Function the store key value pairs in the key index of list"""
    h = self.get_hash(key)
    found = False
  
    for idx, element in enumerate(self.arr[h]):
      if len(element)==2 and element[0] == key:
          self.arr[h][idx] = (key,value)
          found = True
    if not found: #
      self.arr[h].append((key,value))

  def get(self, key):
    """function that return the value stored in the key index"""
    h = self.get_hash(key)
    for element in self.arr[h]:
      if element[0] == key:
        return element[1] 

  def contains(self, key):
    h = self.get_hash(key)
    found = False
    
    for idx, element in enumerate(self.arr[h]):
      if len(element)==2 and element[0] == key:
        found = True
    return found

  def delete(self , key):
    """function that set the value of key to None"""
    h = self.get_hash(key)
    for idx , element in enumerate(self.arr[h]):
      if element[0] == key:
        del self.arr[h][idx]

  def keys(self):
    """function that return all keys in the hash table"""
    keys = []
    for element in self.arr:
        for key in element:
            keys.append(key[0])
    return keys

def left_join_hash(ht_one,ht_two):
    output = []
    for key in ht_one.keys():
        if key in ht_two.keys():
            output.append([key, ht_one.get(key), ht_two.get(key)])
        else:
            output.append([key, ht_one.get(key), None])
            
    for key in ht_two.keys():
        if key not in ht_one.keys():
            output.append([key, None, ht_two.get(key)])
    return output