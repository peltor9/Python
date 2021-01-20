def partition(arr, low, high):
    i = (low-1)         							# index of smaller element
    pivot = arr[high]     								# pivo
    for j in range(low, high): 
               if arr[j] <= pivot:				 # If current element is smaller than or  # equal to pivot 
                       i = i+1					 	# increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i] 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1) 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
def quickSort(arr, low, high):						# Function to do Quick sort
    if len(arr) == 1:
        return arr
    if low < high:
              pi = partition(arr, low, high)			  # pi is partitioning index, arr[p] is now # at right place            
        quickSort(arr, low, pi-1)							# Separately sort elements before
        quickSort(arr, pi+1, high)						# partition and after partition  
arr = [10, 7, 8, 9, 1, 5]								# Driver code to test above
n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i])
