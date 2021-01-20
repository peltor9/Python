##Maximum Value  - Prints the maximum Value from the array
A = [21,25,32,17]
maxval = 0
for i in range(4):
    print(A[i])
    if(A[i]>maxval):
        maxval = A[i]
print(maxval)

##Minimum Value  - Prints the minimum Value from the array
minval = maxval   
for i in range(4):
    if(A[i]<minval):
        minval = A[i]
print(minval)

##Backwards   - Prints the array backwards
A = [21,25,32,17,2,100,5,1]
num = 7
for i in range(8) :
    print(A[num])
    num = num-1
