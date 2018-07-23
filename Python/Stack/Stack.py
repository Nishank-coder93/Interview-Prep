"""
Stack (LIFO)
Stack operations: 
* Stack() Creates a new stack 
* push(item) Pushes item on top of the stack 
* pop() Removes item from top of the stack
* peek() Returns the item on top of the stack 
* isEmpty() Returns boolean value after checking if stack is empy
* size() Returns the number of items on stack
"""

class Stack():
    def __init__(self): 
        self.__stack = []
        self.__size = 0
    
    def push(self,item):
        self.__stack.append(item)
        self.__size += 1
    
    def pop(self): 
        self.__size -= 1
        return self.__stack.pop()
    
    def peek(self):
        return self.__stack[self.__size-1]
    
    def isEmpty(self):
        return self.__size == 0
    
    def size(self):
        return self.__size
    
    def printStack(self):
        print(self.__stack)

if __name__ == "__main__":
    s = Stack()
    s.push('hello')
    s.push('My name')
    s.push('is')
    print(s.pop())
    s.push('Nishank')
    print(s.peek())
    print(s.isEmpty())
    s.printStack()