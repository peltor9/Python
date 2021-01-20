def insertionSort(arr): 
       for i in range(1, len(arr)): 					 # Traverse through 1 to len(arr) 
        key = arr[i]
        j = i-1			 # Move elements of arr[0..i-1], that are    # greater than key, to one position ahead
        while j >=0 and key < arr[j] : 				  # of their current position
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key
arr = [12, 11, 13, 5, 6] 						# Driver code to test above
insertionSort(arr) 
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i])
