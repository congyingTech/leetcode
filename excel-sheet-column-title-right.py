#-*-coding:utf-8-*-
class Solution:
    # @return a string
    def convertToTitle(self, num):
        res, dvd = "", num
        while dvd:
            res += chr((dvd - 1) % 26 + ord('A'))
            dvd = (dvd - 1) / 26 