for i in range(len(A)):          
    min_idx = i 					# Find the minimum element in remaining   # unsorted array
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j                            
    A[i], A[min_idx] = A[min_idx], A[i] 		# Swap the found minimum element with   # the first element 
print ("Sorted array") 				# Driver code to test above 
for i in range(len(A)): 
    print("%d" %A[i]), 
