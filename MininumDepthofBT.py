'''
Created on Mar 1, 2016

@author: wcy
'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def minDepth(self,root):
        if root == None:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right))+1
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right))+1

if __name__ == "main":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    print(Solution().minDepth(root))