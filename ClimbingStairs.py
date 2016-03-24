# -*- coding:utf-8 -*-
'''
Created on Mar 9, 2016

@author: wcy
'''
class Solution(object):
    def climbStairs(self, n):
        #dp是一个长度为n+1的数组
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for x in range(2, n + 1):
            dp[x] = dp[x - 1] + dp[x - 2]
        return dp[n]

if __name__ == "__main__":
    n = 3
    print(Solution().climbStairs(n))
    
