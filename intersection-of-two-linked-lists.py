# -*- coding: utf-8 -*-
'''
Created on Apr 5, 2016

@author: congyingw
'''
''
#1. 得到两个链表的长度
#2. 将长链表向前移动差值
#3. 两个指针一起前进，遇到相同的即是交点，如果没有找到，返回null  
#空间复杂度o(1),时间复杂度o(m+n) 
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        
        
        #求出A的长度
        lenA = Solution().getLength(headA)
        #print('A length % s' % lenA)
        #求出B的长度
        lenB = Solution().getLength(headB)
        #print('B length % s' % lenB)
        #B是长链表,B的头指针向前移动
        while lenB > lenA:
            lenB -= 1
            headB = headB.next
                #print("hereBbig")
            #print(headB.val)
        #A是长链表，A的头指针向前移动
        while lenA > lenB:
            lenA -= 1
            headA = headA.next
                #print("hereAbig")
            #print(headA.val)
        
        #print('此时a的head值 %s' % headA.val)
        #print('此时b的head值%s ' % headB.val)
        #A与B齐头并进，直到链表中不再有元素
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
            
        #如果没有相同的话，返回null
        return None
        
    
    #获得链表长度的函数
    def getLength(self, node):
        #初始化len
        len = 0
        while node:
            len += 1
            node = node.next
        return len
    

if __name__ == "__main__":
    headA, headA.next, headA.next.next, headA.next.next.next  = ListNode(9), ListNode(2), ListNode(3), ListNode(4)
    headB, headB.next, headB.next.next, headB.next.next.next,headB.next.next.next.next = ListNode(2), ListNode(9), ListNode(2), ListNode(3), ListNode(4)
    print(Solution().getIntersectionNode(headA, headB))