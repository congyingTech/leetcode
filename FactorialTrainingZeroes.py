#-*-coding:utf-8-*-
'''
Created on Mar 24, 2016

@author: congyingw
'''

class Solution:
    def trailingZeroes(self, n):
        result = 0
        x = 5
        while n >= x:
            #向下取整floor result = floor(5) + floor(25) + floor(125)....
            result += int(n / x)
            x *= 5
        return result 
            
            
            
         
    
    #求阶乘的函数
#     def Factorial(self, n):
#         if n > 1:
#             result = n * self.Factorial(n - 1)
#             return result
#         else:
#             return 1
            
if __name__ == "__main__":
    n = int(input())
    print(Solution().trailingZeroes(n))