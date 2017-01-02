#Pseudo code from wikipedia: https://en.wikipedia.org/wiki/Comb_sort
def combSort(array,shrinkFactor = 1.3):
    '''performs comb sort on array,default shrink factor is 1.3 return is void'''

    gap = len(array)
    
    while gap>0:
        
        gap=int(gap//shrinkFactor)
        
        for i in range(0,len(array)-gap):
            if array[i]>array[i+gap]:
                array[i],array[i+gap] = array[i+gap],array[i]
