'''
Created on Mar 5, 2016

@author: wcy
'''
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Soulution(object):
    def reverseList(self, head):
        dummy = ListNode(0)
        while head:
            next = head.next
            head.next = dummy.next
            dummy.next = head
            head = next
        return dummy.next
class Solution2:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        [begin, end] = self.reverseListRecu(head)
        return begin
    
    def reverseListRecu(self, head):
        if not head:
            return [None, None]
            
        [begin, end] = self.reverseListRecu(head.next)
        
        if end:
            end.next = head
            head.next = None
            return [begin, head]
        else:
            return [head, head]
        
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print Solution2().reverseList(head)

    
    