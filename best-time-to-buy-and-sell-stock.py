# -*-coding:utf-8 -*-
'''
Created on Apr 12, 2016

@author: congyingw
'''
#题目的大意是找出最大的利润，而最大的利润就是price最小的时候买入，price最大的时候抛出
class Solution:
    def maxProfit(self, prices):
        max_profit, minPrice = 0, float("inf")
        for price in prices:
            minPrice = min(minPrice, price)
            max_profit = max(max_profit, price - minPrice)
        return max_profit

if __name__ == "__main__":
    result = Solution().maxProfit([3,2,1,5,4,2,5,6])
    print(result)
