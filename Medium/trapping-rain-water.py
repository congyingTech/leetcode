#-*- coding:utf-8 -*-
#当前柱状的左边最高的和当前柱状右边最高的进行比较
class Solution(object):
    def trap(self, height):
        #初始化leftmostheight为0，因为从左到右遍历，所以随着i移动，leftmostheight是值会变化的数组
        leftmostheight = [0 for i in range(len(height))]
        #这个是左边最大的
        leftmax = 0 
        for i in range(len(height)):
            if height[i] > leftmax:
                leftmax = height[i]
            leftmostheight[i] = leftmax
        sum = 0 
        rightmax = 0
        #从右向左遍历，随着i移动，rightmax不必再存储到rightmostheight里面，因为leftmostheight已经有了
        for i in reversed(range(len(height))):
            if height[i] > rightmax:
                rightmax = height[i]
            if min(rightmax, leftmostheight[i]) > height[i]:
                sum += min(rightmax, leftmostheight[i]) - height[i]
        return sum
        
    
if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(Solution().trap(height))