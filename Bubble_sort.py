def bubbleSort(arr): 
    n = len(arr) 					  # Traverse through all array elements
    for i in range(n-1): 		  	# range(n) also work but outer loop will repeat one time more than needed.         
        for j in range(0, n-i-1): 		# Last i elements are already in place             
            if arr[j] > arr[j+1] : 		# traverse the array from 0 to n-i-1  # Swap if the element found is greater 
                arr[j], arr[j+1] = arr[j+1], arr[j] 		# than the next element
arr = [64, 34, 25, 12, 22, 11, 90] 			# Driver code to test above 
bubbleSort(arr)
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i])
