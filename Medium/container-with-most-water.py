#-*- coding:utf-8 -*-
#题目要求：这道题是要求找出最大的容量
#先把L1设为最左，R1设为最右，这样宽度最大，然后缩小宽度，那么高度就要比原来高。缩小宽度的逻辑是，如果L1比R1小，那么L1往右移，否则反之
class Solution(object):
    def maxArea(self, height):
        #初始化
        #最左边l的坐标是0，
        l = 0
        #最右边r的初始值是最右边坐标
        r = len(height) - 1
        #print('r value: %s' % r)
        #test:print(r)
        #res 来存放最后的结果
        res = 0
        #tmp存放临时的结果
        tmp = 0
        while l < r:
            
            #r-l是宽度， min()里是左右最小的高度，因为容量取决于短板
            tmp = min(height[l], height[r]) * (r - l)
            #res = max(res, min(height[r], height[l]) * (r - l))
            
            #test:print(tmp)
            #如果tmp比较大的话，
            if tmp > res:
                res = tmp
            if height[l] < height[r]:
            #左边的小于右边的，容量取决于左边，于是从左边找有没有更大的高度
                lastl = height[l]
                while l < r and height[l] <= lastl:
                    l += 1
            else:
            #右边的小于左边的，取决于右边,从右边找有没有更大的高度
                lastr = height[r]
                while l < r and height[r] <= lastr:
                    r -= 1
        return res

if __name__ == '__main__':
    height = [1, 2, 3, 3,4, 3, 2, 1, 5]
    print(Solution().maxArea(height))
                
            