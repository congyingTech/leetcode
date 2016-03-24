# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def isBalanced(self, root):
        return self.getHeight(root) >= 0
        
    def getHeight(self, root):
        if root is None:
            return 0
        left_h, right_h = self.getHeight(root.left), self.getHeight(root.right)
        if left_h < 0 or right_h < 0 or abs(left_h - right_h) > 1:
            return -1
        return max(left_h, right_h) + 1

if __name__ == "__main__":
    HeadNode = TreeNode(0)
    HeadNode.left = TreeNode(1)
    HeadNode.left.left = TreeNode(2)
    HeadNode.left.left.left = TreeNode(2)
    print(Solution().isBalanced(HeadNode))