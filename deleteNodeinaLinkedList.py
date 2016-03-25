'''
Created on Mar 2, 2016

@author: wcy
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

'''class Solution:
    def deleteNode(self, node):
        if node == None:
            return None
        if node.val == node:
            node.val = node.next.val
        else:
            node = node.next
        return node'''
class Solution:
    def deleteNode(self, node):
        if node and node.next:
            node.val = node.next.val
            node.next = node.next.next
  
       
if __name__ == "__main__":
    first = ListNode(1) 
    first.next = ListNode(2)
    first.next.next = ListNode(3)
    first.next.next = ListNode(4)
    node_to_delete = ListNode(3)
    newlist = Solution().deleteNode(node_to_delete)

    
    