'''
Created on Mar 3, 2016

@author: wcy
'''
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    #DFS
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is not None and q is not None:
            return p.val ==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        return False
    
if __name__ == "__main__":
    root1, root1.left, root1.right = TreeNode(1), TreeNode(2), TreeNode(3)
    root2, root2.left, root2.right = TreeNode(2), TreeNode(2), TreeNode(3)
    print (Solution().isSameTree(root1, root2))