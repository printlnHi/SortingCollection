#Pseudocode from wikipedia:https://en.wikipedia.org/wiki/Cocktail_shaker_sort
def rippleSort(array):
    '''Performs ripple sort on array, return is void'''
    isSorted = False
    
    while not isSorted:
        
        isSorted = True
        
        for i in range(len(array)-1):
            if array[i]>array[i+1]:
                isSorted = False
                array[i],array[i+1]=array[i+1],array[i]
                
        for i in range(len(array)-2,0,-1):
            if array[i]>array[i+1]:
                isSorted = False
                array[i],array[i+1]=array[i+1],array[i]
