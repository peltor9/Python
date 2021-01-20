class Stack():
    def push(self,item):                                    ## Push: add an element to the top of stack
        self.items.append(item)
    def pop(self):                                          ## Pop: delete the element at the top of stack
        return self.items.pop()
    def show_stack(self):                                   ## Show full stack
        return self.items

obj = Stack()
def evaluatePostfix(exp): 
    for i in exp:
        if i.isdigit():                                      ## Check whether entered character is a number
            obj.push(i)                                      ## push the number to stack
        else: 
            val1 = obj.pop()                                ## Check if the scanned character is an operator
            val2 = obj.pop()                                ## pop two elements from stack and apply it. 
            obj.push(str(eval(val2 + i + val1))) 

    return int(obj.pop()) 
exp = str(input("Enter a postfix expression: "))
print ("Postfix evaluation result: "+ str(evaluatePostfix(exp))) 
