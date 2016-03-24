'''
Created on Mar 24, 2016

@author: congyingw
'''
class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        result = 0
        while n > 0:
            result += int(n / 5)
            print(result)
            n /= 5
        return result

if __name__ == "__main__":
    print(Solution().trailingZeroes(120))
