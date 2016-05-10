#-*-coding:utf-8-*-
class Solution(object):
    def firstBadVersion(self, n):
        left, right =1, n
        while left <= right:
            mid = (left + right) / 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
