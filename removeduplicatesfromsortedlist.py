# -*- coding:utf-8 -*-
'''
Created on Mar 9, 2016

@author: wcy
'''
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
class Solution:
    def deleteDuplicates(self, head):
        cur = head
        while cur:
            runner = cur.next
            while runner and runner.val == cur.val:
                runner = runner.next
            cur.next = runner
            cur = runner
        return head

if __name__ == "__main__":
    first = ListNode(1)
    first.next = ListNode(2)
    first.next.next = ListNode(2)
    first.next.next.next = ListNode(3)
    Solution().deleteDuplicates(first)
    while first:
        print first.val
        first = first.next
   
