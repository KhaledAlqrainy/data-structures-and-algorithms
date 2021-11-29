from Data_Structure.hashTable.hashmap import HashTable
def hashmap_left_join(key, key2):

    result = []

    for i in key:
        if i:
            current = i.head
            while current:
                result += [[current.key, current.value],]

    return result
