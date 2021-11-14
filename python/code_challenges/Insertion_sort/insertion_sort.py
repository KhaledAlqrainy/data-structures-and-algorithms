def insertion_sort(list):

    for i in range(1, len(list)):
        value = list[i]
        i -= 1
        
        while i >= 0:
            if value < list[i]:
                list[i+1] = list [i] 
                list[i] = value 
                i -= 1
            else:
                break
    return list

a = [20,18,12,8,5,-2]
insertion_sort(a)
print(a)