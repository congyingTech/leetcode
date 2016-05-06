# -*-coding:utf-8 -*-

#numRows = 3
# P   A   H   N (0 4 8 12)
# A P L S I I G (1 3 5 7 9 11)
# Y   I   R     (2 6 10)

#numRows = 4
#P     I     N  (0 6 12)
#A   L S   I G  (1 5 7 11 13)
#Y A   H R      (2 4 8 10)
#P     I        (3 9)

#input
#0 1 2 3 4 5 6 7 8 9 10 11 12 13
#P A Y P A L I S H I  R  I  N  G
#output
#0 4 8 12 1 3 5 7 9 11 13 2 6 10
#P A H  N A P L S I  I  G Y I  R

#由输入输出可以看到,首尾的下标值是隔了4个数的，
#除了首尾之外的中间的几行，是隔了两个数的
class Solution:
    def convert(self, s, numRows):
        
        if numRows == 1:
            return s
        #由下标的排序的规律可以知道,step的2*numRows - 2 
        step, zigzag = 2 * numRows - 2, ""
        for i in range(numRows):
            for j in range(i, len(s), step):
                zigzag += s[j]
                #这是 除了首尾两行之外，中间的两行的规律
                if 0 < i < numRows - 1 and j + step - 2 * i < len(s):
                    zigzag += s [j + step -2 * i]
        return zigzag
    
if __name__ == "__main__":
    print(Solution().convert("abcdbgksf", 4))