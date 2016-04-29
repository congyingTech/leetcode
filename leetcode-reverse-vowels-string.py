#-*- coding:utf-8 -*-
class Solution(object):
    #这里使用双指针的方法
    def revereseVowels(self,s):
        VOWELS = ('a', 'e', 'i', 'o', 'u')
        size = len(s)
        left, right = 0, size - 1
        #将string转换为list
        ls = list(s)
        while True:
            while left < size and s[left].lower() not in VOWELS:
                left += 1
            while right >= 0 and s[right].lower() not in VOWELS:
                right -= 1
            if left >= right: break
            ls[left], ls[right] = ls[right], ls[left]
            left, right = left + 1, right - 1
        #list to string 
        return ''.join(ls)


if __name__ == "__main__":
    s = "leetcode"
    print(Solution().revereseVowels(s))
    
    
    
    
   