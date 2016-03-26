#-*- coding:utf-8 -*-

#按照题目的要求，应该交换两个相邻的结点

class ListNode(object):
    def __init__(self, val):
        self.next = None
        self.val = val
    
class Solution(object):
    def swapPairs(self, head):
        #虚拟出来一个头结点dummy,初始化为0
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next and current.next.next:
            next_one = current.next
            next_two = current.next.next
            next_three = current.next.next.next
            #开始swap
            current.next = next_two
            next_two.next = next_one
            next_one.next = next_three
            #交换完毕 current 后移两个
            #current = next_two这行代码是错的，因为在交换结点完毕后，位于current后移两个位置的结点是next_one
            current = next_one
        return dummy.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next, head.next.next, head.next.next.next = ListNode(2), ListNode(3), ListNode(4)
    new_head = Solution().swapPairs(head)
    print(new_head)
