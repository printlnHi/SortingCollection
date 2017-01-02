def mergeSort(array):
    '''Performs in-place merge-sort without the recursive call of other functions
    return is void'''
    
    subarrays = [list([i]) for i in array]
    while len(subarrays)>1:
        
        mergedSubarrays = []
        
        for index in range(0,len(subarrays)-1,2):
            mergedSubarray=[]
            
            firstSubarray = subarrays[index]
            secondSubarray = subarrays[index+1]
            i = 0
            j = 0
            
            while len(firstSubarray)>i and len(secondSubarray)>j:
                if firstSubarray[i]>secondSubarray[j]:
                    mergedSubarray.append(secondSubarray[j])
                    j+=1
                else:
                    mergedSubarray.append(firstSubarray[i])
                    i+=1

            while len(firstSubarray)>i:
                mergedSubarray.append(firstSubarray[i])
                i+=1
            
            while len(secondSubarray)>j:
                mergedSubarray.append(secondSubarray[j])
                j+=1
            
            mergedSubarrays.append(mergedSubarray)

        if len(subarrays)%2==1:
            mergedSubarrays.append(subarrays[-1])
        subarrays = mergedSubarrays


    for index,value in enumerate(subarrays[0]):
        array[index] = value


a = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0]
mergeSort(a)
