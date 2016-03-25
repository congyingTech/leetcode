# -*- coding:utf-8 -*-
'''
Created on Mar 16, 2016

@author: wcy
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        
        while stack:
            p, q = stack.pop(), stack.pop()
            
            if p is None and q is None:
                continue
            
            if p is None or q is None or p.val != q.val:
                return False
            
            stack.append(p.left)
            stack.append(q.right)
            
            stack.append(p.right)
            stack.append(q.left)
            
        return True
    
#my idea:   
class Solution2(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isSymmetricRecu(root.left, root.right)
    
    def isSymmetricRecu(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isSymmetricRecu(left.left, right.right) and self.isSymmetricRecu(left.right, right.left)
        
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(3)
    root.right.left = TreeNode(4)
    print(Solution2().isSymmetric(root))
    
    
            
                
                
                
        
        
        
        
        
        





