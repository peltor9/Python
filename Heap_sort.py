def swap(i, j):                    
    arr[i], arr[j] = arr[j], arr[i]             ## Swap function

def heapify(end,i):                             ## Initialize largest as root
    l=2 * i + 1                                 ## left = 2*i + 1 
    r=2 * (i + 1)                               ## right = 2*i + 2  
    max=i   
    if l < end and arr[i] < arr[l]:            
        max = l   
    if r < end and arr[max] < arr[r]:   
        max = r   
    if max != i:   
        swap(i, max)   
        heapify(end, max)   

def heapSort():                                 ##  Calling for heapsort function
    end = len(arr)   
    start = end // 2 - 1 
    for i in range(start, -1, -1):   
        heapify(end, i)   
    for i in range(end-1, 0, -1):   
        swap(i, 0)   
        heapify(i, 0)   

arr = [ 245, 312, 124, 56, 156, 452, 223, 23 ]
heapSort()
print(arr)
