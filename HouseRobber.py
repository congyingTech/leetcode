# -*- coding:utf-8 -*-
class Solution(object):
    def rob(self, num):
        size = len(num)
        #dp-list初始化,长度为size+1,第一个值是num的第一个值
        dp = [0] * (size + 1)
        if size :
            dp[1] = num[0]
        for i in range(2,size + 1):
            #动态规划:找出dp[i]之前的最优解
            dp[i] = max(dp[i-1], dp[i-2] + num[i - 1])
        return dp[size]

if __name__ =="__main__":
    num = [1,2,3,4,5]
    print(Solution().rob(num))