#-*- coding:utf-8 -*-

#又是超时的一个杰作 呵呵呵呵呵
class Solution(object):
    def topKFrequent(self, nums, k):
        #sortednums = sorted(nums)
        nosamenums = set(nums)
        #countdict = dict() 这样使用会有UnboundLocalError: local variable 'dict' referenced before assignment
        countdict = {}
        res = []
        #初始化countdict
        for e in nosamenums:
            countdict[e] = 0
#test:        
#       for k in countdict:
#           print(k)
        #test : print(countdict)
        for key in countdict:
            for i in nums:
                if i == key:
                    countdict[key] += 1
        countlist = sorted(countdict.items(), key=lambda d:d[1], reverse = True)
        #test : print(countlist)
        for n in range(k):
            res.append(countlist[n][0])
        return res
            
        
        
        
if __name__ == "__main__":
    #nums = [1, 2, 3 , 1, 3, 1]
    nums = [1,1,1,2,2,3]
    print(Solution().topKFrequent(nums, 2))
