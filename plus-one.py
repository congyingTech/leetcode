#-*-coding:utf-8-*-

#本题目的意思是进位加法997+1=998  999+1=1000
class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        #carry 是进位的意思
        carry = 1
        for i in reversed(range(len(digits))):
            digits[i] += carry
            carry = digits[i] / 10
            digits[i] %= 10
        
        if carry:
            digits = [1] + digits
        return digits

if __name__ == "__main__":
     print(Solution().plusOne([9, 9, 9, 8]))