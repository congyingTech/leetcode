# -*- coding:utf-8 -*-
'''
Created on Mar 9, 2016

@author: wcy
'''

class Solution(object):
    def isUgly(self, num):
        if num <= 0:
            return False
        for i in [2,3,5]:
            #num除以i能除尽的时候,都要一直除以i
            while num % i == 0:
                num /= i
        #如果除到最后num是1说明可以除尽2or3or5, 则这个数是丑数
        return num==1    
if __name__ == "__main__":
    num = 12
    print(Solution().isUgly(num))