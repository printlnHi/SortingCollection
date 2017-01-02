#Pseudo code from Introduction to Algorithms, 2008
def merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L = []
    R = []
    for i in range(1,n1+1):
        L.append(A[p+i-1])
    for j in range(1,n2+1):
        R.append(A[q+j])
    R.append(float("inf"))
    L.append(float("inf"))
    i = 0
    j = 0
    for k in range(p,r+1):
        if L[i]<=R[j]:
            A[k]  = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1

def mergeSort(A,p=0,r=None):
    '''Performs a merge sort on A, return is void'''
    if r == None:
        r = len(A)-1
    if p<r:
        q = int((p+r)/2)
        mergeSort(A,p=p,r=q)
        mergeSort(A,p=q+1,r=r)
        merge(A,p,q,r)
