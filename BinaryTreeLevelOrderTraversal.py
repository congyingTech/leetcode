#-*-coding:utf-8-*-
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def levelOrder(self, root):
        result = []
        #current结点list一定是一个list类型,因为current不一定只有一个结点
        current = [root]
        if root is None:
            return result
        while current:
            #vals[] 是记录该层的结点的value的,存的是value值,同时,我们要能够遍历下一层的结点,next_level=[],存的是TreeNode
            #此处一定要写两个[]
            vals, next_level = [], []
            #因为该层的结点可能不止一个,所以要进行for循环
            for i in current:
                #将i结点的值加入vals
                vals.append(i.val)
                #通过current的左右结点是否存在,得到下一层的结点
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            #当前结点加入完毕后,1)将vals加入到result中;2)将current指向下一层
            result.append(vals)
            current = next_level
        return result

    
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    print(Solution().levelOrder(root))
