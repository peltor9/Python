def shellSort(arr):  
    n = len(arr) 							# Start with a big gap, then reduce the gap
    gap = n/2
    
    # Do a gapped insertion sort for this gap size. 
    # The first gap elements a[0..gap-1] are already in gapped  
    # order keep adding one more element until the entire array     # is gap sorted 
    
    while gap > 0:  
        for i in range(gap,n): 					 # add a[i] to the elements that have been gap sorted
            temp = arr[i] 						# save a[i] in temp and make a hole at position  
            # location for a[i] is found 
            j = i 						 # shift earlier gap-sorted elements up until the correct 
            while  j >= gap and arr[j-gap] >temp: 				# location for a[i] is found 
                arr[j] = arr[j-gap] 
                j -= gap 
                       arr[j] = temp 						 # put temp (the original a[i]) in its correct location 
        gap /= 2    
arr = [ 12, 34, 54, 2, 3] 							# Driver code to test above   
n = len(arr) 
print ("Array before sorting:") 
for i in range(n): 
    print(arr[i]),   
shellSort(arr)   
print ("\nArray after sorting:") 
for i in range(n): 
    print(arr[i])
