#-*-coding:utf-8-*-
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def levelOrder(self, root):
        result = []
        
        current = root
        if current is None:
            return result
        while current:
            vals = []
            vals.append(current.val)
            if current.left:
                self.levelOrder(current.left)
            if current.right:
                current = current.right
                self.levelOrder(current.right)
            result.append(vals)
            print(vals)
        return result
    
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    print(Solution().levelOrder(root))
