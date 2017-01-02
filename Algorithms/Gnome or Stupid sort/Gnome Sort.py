#Pseudocode from https://en.wikipedia.org/wiki/Gnome_sort
def gnomeSort(array):
    '''performs a in-place sort on array via gnome sort
    return is void'''
    position = 0
    while position<len(array):
        if position ==0 or array[position]>=array[position-1]:
            position+=1
        else:
            array[position],array[position-1] = array[position-1],array[position]
            position-=1
