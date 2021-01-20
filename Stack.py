## Example Array
stack = [ ]

## Top: return the element at the top of stack
def top(num):
    top = top + num
    return

## Push: add an element to the top of stack
def push() :
    ele = input("add element to stack: ")
    top_pointer = top(1)
    stack.append(ele)

## Pop: delete the element at the top of stack
def pop():
    print("pop element: " + stack[top])
    top_pointer = top(-1)

## Example
top = -1
for i in range(5):
    num = eval( input("Add number to stack: ") )
    top = top+1
    stack.append(num)
    print("top pointer is: " + str(top))
    
for i in range (5):
    print(stack[top])
    top = top-1
