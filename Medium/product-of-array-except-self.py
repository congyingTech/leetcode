#-*-coding:utf-8-*-
#上一种方法超时，常数时间
#参考了答案之后：从左边和右边分别计算乘积

#但是这个并不是很理解TnT 每每到这个时候智商感人~

class Solution(object):
    def productExceptSelf(self, nums):
        size = len(nums)
        output = [1] * size
        left = 1
        for i in range(size - 1):
            left *= nums[i]
            output[i + 1] *= left
        print(output)    
        
        right = 1
        for x in range(size - 1, 0, -1):
            right *= nums[x]
            output[x - 1] *= right
        return output
    
    
if __name__ == "__main__":
    print(Solution().productExceptSelf([1,2,3,4]))
    
    
    