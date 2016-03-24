# -*-coding:utf-8 -*-
'''
Created on Mar 17, 2016

@author: wcy
'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def levelOrderBottom(self, root):
        if root is None:
            return []
        result, current = [],[root]
        while current:
            next_level, vals = [], []
            for node in current:
                #将current结点的值存入vals中
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            print(vals)
            #key is here!:将vals值插入index为0的头部
            result.insert(0, vals)
            print(result)
        return result

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    print(Solution().levelOrderBottom(root))
    
                  
                



