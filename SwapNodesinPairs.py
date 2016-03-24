#-*- coding:utf-8 -*-

#这是错的，因为要求的是交换相邻的Node，我这是交换相邻的data
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def swapPairs(self, head):
        if head is None:
            return head
        p = head
        while p:
            if p.next:
                swapVal = p.val
                p.val = p.next.val
                p.next.val = swapVal
                p = p.next.next
            else:
                break
        return p
    
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    Solution().swapPairs(head)
    while head:
        print(head.val)
        head = head.next
        
