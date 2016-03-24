
'''
Created on Mar 2, 2016

@author: wcy
'''
class Solution(object):
    def moveZeroes(self,nums):
        count = 0
        for x in range(len(nums)):
            if nums[x] == 0:
                count += 1
                del nums[x]
        print ('0 nums=', count)
        print(nums)
        
        for j in range(0,count-1):
            nums.append(0)
            print nums
        return nums
if __name__ == "__main__":
    list = [1,2,0,3,4]
    print(list)
    newlist = Solution().moveZeroes(list) 
    print("result")
    print(newlist)