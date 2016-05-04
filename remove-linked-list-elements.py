# -*- coding:utf-8 -*-
# Definition for singly-linked list.

#未完成！！！

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        #如果头结点的值就是要删除的值，则头结点直接指向下一个结点
        p = head
        while p.next:
            if p.val == val:
                head = head.next
            if p.next.val == val and p.next.next:
                #p.next是要删除的结点，删除p.next
                p.next = p.next.next
                p = p.next
            #要删除的结点是尾结点
            elif p.next.val == val and p.next.next == None:
                p.next = None
                p = p.next
            else:
                p = p.next
        return head

if __name__ == "__main__":
    head = ListNode(1)
    head.next, head.next.next, head.next.next.next,head.next.next.next.next = ListNode(1),ListNode(3),ListNode(1),ListNode(5)
    Solution().removeElements(head, 1)
    while head:
        print(head.val)
        head = head.next
    
    
    
    
    
                
        