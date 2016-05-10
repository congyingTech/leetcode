# -*-coding:utf-8-*-

class Solution(object):
    def twoSum(self, nums, target):
        length = len(nums)
        for i in range(0, length):
            #test:print(i)
            #test:print(nums[i])
            for j in range(i + 1, length):
                #test:print(j)
                #test:print(nums[j])
                if nums[i] + nums[j] == target:
                    return [i, j]
    
    
if __name__ == "__main__":
    print(Solution().twoSum([3, 2, 4], 6))