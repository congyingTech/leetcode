#-*-coding:utf-8-*-
# 给定一个整数数组，除一个元素只出现一次外，其余各元素均出现两次。找出那个只出现一次的元素。
# 
# 注意：
# 
# 你的算法应该满足线性时间复杂度。可以不使用额外的空间完成此题吗？

#按位异或运算符：当两对应的二进位相异时，结果为1

from _functools import reduce
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x,y: x ^ y, nums)
        #return reduce(operator.xor,nums)
    
if __name__ == "__main__":
    nums = [1,1,2,3,4,5]
    print(Solution().singleNumber(nums))

