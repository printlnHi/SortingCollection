#Pseudo code according to introduction to algorithms
#Introduction to algorithms version runs in thetha(N^2) as opposed to wikipedia version
def bubbleSort(array):
    '''performs bubble sort on array, returnis void'''
    for i in range(len(array)-2):
        for j in range(len(array)-1,i,-1):
            if array[j]<array[j-1]:
                array[j],array[j-1]=array[j-1],array[j]
