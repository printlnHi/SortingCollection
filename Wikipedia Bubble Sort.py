#Bubble sort according to wikipedia (https://en.wikipedia.org/wiki/Bubble_sort)
#Runs in worst case O(N^2),average case O(N^2),best case O(N)
def bubbleSort(array):
    '''sorts array via bubble sort, return is void'''
    swapOccured = True
    while swapOccured:
        swapOccured = False
        for i in range(1,len(array)):
            if array[i-1]>array[i]:
                swapOccured = True
                array[i-1],array[i] = array[i],array[i-1]
