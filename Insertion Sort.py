def insertionSort(array):
    n = len(array)
    for i in range(n):
        x = array[i]
        for index in range(i):
            item  = array[index]
            if item>x:
                for j in range(i-1,index-1,-1):
                    array[j+1]=array[j]
                array[index] = x
                break
