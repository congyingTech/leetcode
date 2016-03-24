# -*- coding:utf-8 -*-
'''
Created on Mar 24, 2016

@author: congyingw
'''
#测试链表交换能不能只交换值

class LN:
    def __init__(self, val):
        self.next = None
        self.val = val

    
def printLN(head):
    while head:
        print(head.val)
        head = head.next

if __name__ == "__main__":
    head = LN(1)
    head.next = LN(2)
    head.next.next = LN(3)
    head.next.next.next = LN(4)
    printLN(head)
    
    temp = head.val
    head.val = head.next.val
    head.next.val = temp
    
    printLN(head)
    
    temp = head.next.next.val
    head.next.next.val = head.next.next.next.val
    head.next.next.next.val = temp
    
    printLN(head)
    
    
    
    
    
        
    