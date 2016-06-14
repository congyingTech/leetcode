#-*-coding:utf-8-*-
#题目的意思就是：输出除了num[i]之外的数的乘积
#input=[1,2,3,4] output=[24,12,8,6]

#这种方法超时了。结果是正确的

from _functools import reduce
class Solution(object):
    def productExceptSelf(self, nums):
        output = []
        for i,num in enumerate(nums):
            #test iterable : print(isinstance(nums.remove(num), Iterable))
            #test type : print(type(nums.remove(num)))
            nums.remove(num)
            #test : print(nums)
            res = reduce(lambda x,y:x*y , nums)
            nums.insert(i,num)
            output.append(res)
        return output
    
    
if __name__ == "__main__":
    print(Solution().productExceptSelf([0,0,0]))