# -*-coding :utf-8 -*-
'''
Created on Mar 13, 2016

@author: wcy
'''

class Queue(object):
    def __init__(self):
        self.inStack = []
        self.outStack = []
    #push    
    def push(self,x):
        self.inStack.append(x)
    #pop,peek get head     
    def pop(self):
        self.peek()
        self.outStack.pop()
    #peek
    def peek(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]
    
    #empty
    def empty(self):
        return len(self.inStack) + len(self.outStack) == 0
    
if __name__ == "__main__":
    for i in range(0,3):
        stack = Queue().push(i)
    while stack is not None:
        stack.pop()
        print stack                               
    
    