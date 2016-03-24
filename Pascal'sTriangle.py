# -*-coding:utf-8 -*-
class Solution:
    def generate(self, numRows):
        #结果存放在result list中
        result = []
        #i是控制行变化的
        for i in range(0, numRows):
            #每行都是一个list
            result.append([])
            for j in range(0, i + 1):
                #当j位于首尾时
                if j in (0, i):
                    result[i].append(1)
                else:
                    result[i].append(result[i-1][j-1] + result[i-1][j])
                
        return result
                    
                
        
    


if __name__ == "__main__":
    #输入杨辉三角的行数
    numRows = int(input())
    print(Solution().generate(numRows))