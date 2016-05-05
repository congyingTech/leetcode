# -*- coding:utf-8 -*-
'''
Created on May 5, 2016

@author: congyingw
'''
#找二叉树的路径，首先就要遍历二叉树，遍历二叉树的方式有两种，深度优先遍历（DFS）和广度优先遍历
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        res, path = [], []
        if root is None:
            return res
        self.dfs(root, path, res)
        return res
    
    def dfs(self, root, path, res):
        if root is None:
            return
        #当左右孩子都没有的时候，整理结果
        if root.left is None and root.right is None:
            ans = ""
            for n in path:
                ans += str(n.val) + "->"
            res.append(ans + str(root.val)) 
            
        if root.left:
            path.append(root)
            self.dfs(root.left, path,res)
            path.pop()
            
        if root.right:
            path.append(root)
            self.dfs(root.right, path, res)
            path.pop()
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    print(Solution().binaryTreePaths(root))     
        
