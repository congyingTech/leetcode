# -*- coding:utf-8 -*-
#回文字linkedlist的判断
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        head_list = []
        while head:
            head_list.append(head.val)
            head = head.next
        cnt = 0
        for i in range(len(head_list)):
            if head_list[i] == head_list[len(head_list) - i - 1]:
               cnt += 1
        
        if cnt == len(head_list):
            return True
        else:
            return False  
        
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    #head.next.next.next = ListNode(1)
    print(Solution().isPalindrome(head))
