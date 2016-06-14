'''
Created on Jun 1, 2016

@author: congyingw
'''

#贪心法：局部最优化
class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(len(prices) - 1):
            profit += max(0, prices[i + 1] - prices[i])
        return profit


if __name__ == '__main__':
    result = Solution().maxProfit([2,3,54,5,2,56])
    print(result)

