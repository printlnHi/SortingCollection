#Pseudo code from wikipedia:https://en.wikipedia.org/wiki/Stooge_sort
def stoogeSort(array,i = 0,j = None):
    '''performs stooge sort on array, return is void'''
    if j==None:
        j = len(array)-1

    if array[j]<array[i]:
        array[j],array[i] = array[i],array[j]

    if (j - i) > 1:
        t = (j - i + 1)//3
        
        stoogeSort(array,i = i,j = j-t)
        stoogeSort(array,i = i+t,j = j)
        stoogeSort(array,i = i,j = j-t)
