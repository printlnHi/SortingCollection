def selectionSort(array):
    '''performs selection sort on array, return is void'''
    for i in range(len(array)-1):
        smallest = i

        for j in range(i,len(array)):
            if array[j]<array[smallest]:
                smallest = j

        array[i],array[smallest] = array[smallest],array[i]
