def partition(array, low, high):
    
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quickSort(array):
    
    def qS(array, low, high):

        if low < high:
            pi = partition(array, low, high)
            qS(array, low, pi - 1)
            qS(array, pi + 1, high)

    qS(array, 0, len(array) - 1)