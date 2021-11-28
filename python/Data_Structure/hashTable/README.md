# Hash table

* Hash table is a special collection that is used to store key-value items. So instead of storing just one value like the stack, array list and queue, the hash table stores 2 values. These 2 values form an element of the hash table. Below are some example of how values of a hash table might look like.


## Challenge 

* Create a list with 1024 None elements, whenever we add a value it will check if it's existed in the location, if there is not(none) it will create a linked list and insert to it, else it will add to the existing linked list.

## Approach & Efficiency

Big O :

time -> O(1)
space -> O(1)

## API 

* Create a hashtable with the following methods:

    - add which takes in both the key and value. Hash the key, and add the key and value pair to the table, handling collisions as needed.

    - get that takes in the key and returns the value from the table.

    - contains that takes in the key and returns a boolean, indicating if the key exists in the table already.

    - hash that takes in an arbitrary key and returns an index in the collection.

Insert key, value pair in the hashtable.
Hash keys to determine is which index it should be added.

