#-*- coding:utf-8 -*-

class Solution(object):
    def getHint(self, secret, guess):
        resultA = 0
        resultB = 0
        for i,value in enumerate(secret):
            if secret[i] == guess[i]:
                resultA += 1
            else:
                resultB += 1
        return "%sA%sB" % (resultA,resultB)


if __name__ == "__main__":
    secret = "1123"
    guess = "0111"
    print(Solution().getHint(secret, guess))