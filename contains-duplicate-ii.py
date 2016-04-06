#-*- coding:utf-8 -*-
#算法思想：用Python中的dict 或者 enumerate得到下标，进行下标的比较
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        numDict = {}
        for i,num in enumerate(nums):
            print(i,num)
            if num not in numDict:
                numDict[num] = i
            else:
                if i-numDict[num] <= k:
                    return True
                #update 了 最新的重复元素的位置
                numDict[num] = i
        print(numDict)
        return False 
            
if __name__ == "__main__":
    nums = [1,2,1,9,4,11,6,1]
    print(Solution().containsNearbyDuplicate(nums, 1))