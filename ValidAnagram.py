'''
Created on Mar 3, 2016

@author: wcy
'''
class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
    
if __name__ =="__main__":
    s = "nas"
    t = "san"
    print(Solution().isAnagram(s, t))