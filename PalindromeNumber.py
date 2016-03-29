# -*-coding:utf-8 -*-
'''
Created on Mar 29, 2016

@author: congyingw
'''
import math
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        #count 作为记录最高位数在第几位的计数器
        count, temp = 0, x
        while temp:
            temp = int(temp / 10)
            count += 1
        copy,result = x, 0
        while copy:
            reverse = copy % 10
            copy = int(copy / 10)
            #test
            #print("从后往前： reverse:%s copy:%s count:%s" % (reverse, copy, count))
            result = result + reverse * math.pow(10, count-1)
            count = count - 1
        return x == result
    
if __name__ == "__main__":
    print(Solution().isPalindrome(123123))