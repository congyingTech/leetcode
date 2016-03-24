#-*- coding:utf-8 -*-
'''
Created on Mar 17, 2016

@author: wcy
'''
class Solution(object):
    def removeElement(self, nums, val):
        i, last = 0, len(nums) - 1
        while i <= last:
            if nums[i] == val:
                #将要删除的元素移到list尾部,将list的长度减一,就自动删除了元素
                nums[i],nums[last] = nums[last],nums[i]
                last -= 1
            else:
                i += 1
        return last + 1
                
if __name__ == "__main__":
    print(Solution().removeElement([1,2,33,44,5,2,1], 2))
                