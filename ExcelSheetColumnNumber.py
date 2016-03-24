 '''
Created on Mar 3, 2016

@author: wcy
'''
class Solution:
    def titleToNumber(self, s):
        #ans is sum of 'AA'
        ans = 0
        for e in s:
            ans = ans*26 + ord(e) - ord('A') + 1
        return ans
