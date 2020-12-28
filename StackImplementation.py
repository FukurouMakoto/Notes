class Stack:
    def __init__(self):
        self.StackList = []
    
    # [1, 2, 3, 4, 5]

    #Is stack empty?
    def is_empty(self):
        return len(self.StackList) == 0

    #Return the number of elements in the stack
    def size(self):
        if self.is_empty():
            return "Stack Empty"
        else:
            return len(self.StackList)
    
    #Push an element onto the stack
    def push(self, element):
        self.StackList.append(element)

    #Pop an element off the stack 
    #Throw an error if the stack is empty
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            self.StackList.pop()
    
    #Peek the top of the stack without removing an element
    #Throw an error if stack is empty
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.StackList[-1]