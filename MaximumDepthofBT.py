'''
Created on Mar 1, 2016

@author: wcy
'''
class TreeNode:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None

class resolution:
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)    
    
    print resolution().maxDepth(root)

          

        