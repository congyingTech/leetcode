#-*-coding:utf-8 -*-

class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None
    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution(object):
    def removeNthFromEnd(self, head, n):
        if n == 0:
            return head
        if head == None:
            return None
        len = 0
        temp1 = head
        while(temp1):
            len += 1
            temp1 = temp1.next
        position = len - n - 1
        print(position)
        
        if position < 0:
            return head.next
        
        temp2 = head
        while position > 0:
            temp2 = temp2.next
            position -= 1
        if temp2.next.next != None:
            temp2.next = temp2.next.next
        else :
            temp2.next = None
        return head
            
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    #head.next, head.next.next, head.next.next.next,head.next.next.next.next = ListNode(2),ListNode(3),ListNode(4),ListNode(5)
    n = 2
    newhead = Solution().removeNthFromEnd(head, n)
    while(head):
        print(head.val)
        head = head.next


    