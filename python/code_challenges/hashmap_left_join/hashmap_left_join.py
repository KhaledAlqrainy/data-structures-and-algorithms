
def hashmap_left_join(key, key2):

    result = []

    for i in key.keys():
        if i in key2.keys():
            result.append([i, key[i], key2[i]])
        else:
            result.append([i, key[i], "None"])
    return result
