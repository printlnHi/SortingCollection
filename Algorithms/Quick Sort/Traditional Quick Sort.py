#Pseudo code from Introduction to Algorithms, 2008
def quickSort(array,p=0,r=None):
    '''quick-sorts the array, return is void'''
    if r==None:
        r = len(array)-1

    if p<r:
        q = partition(array,p,r)
        quickSort(array,p=p,r=q-1)
        quickSort(array,p=q+1,r=r)

def partition(array,p,r):
    x = array[r]
    i = p-1

    for j in range(p,r):
        if array[j]<=x:
            i+=1
            array[i],array[j] = array[j],array[i]

    array[i+1],array[r] = array[r],array[i+1]

    return i+1
