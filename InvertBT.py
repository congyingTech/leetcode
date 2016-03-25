'''
Created on Mar 1, 2016

@author: wcy
'''
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def invertBT(self, root):
        if root is None:return None
        if root.left:
            self.invertBT(root.left)
        if root.right:
            self.invertBT(root.right)
        root.left, root.right = root.right, root.left
        return root
     
        
#we can add a function of level traversal here
         

if __name__ == "main":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)    
    newroot = Solution().invertBT(root)

    