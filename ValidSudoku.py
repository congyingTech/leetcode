#-*- coding:utf-8 -*-
'''
Created on Mar 30, 2016

@author: congyingw

'''



#Sudoku的要求有三条：每行的数只出现一次，每列的数只出现一次，每个九宫格数只出现一次。
#所以我们要验证这三个条件逐个遍历一遍。


class Solution:
    def isValidSudoku(self, board):
        for i in range(0, 9):
            #第i行（固定的行）j列  or 第j行i列（固定的列）
            if not self.isValidList([board[i][j] for j in range(0,9)]) or not self.isValidList([board[j][i] for j in range(0, 9)]):
                return False
        
        #检查第三条：九宫格里面是否出现重复，
        for i in range(0, 3):
            for j in range(0, 3):
                if not self.isValidList([board[m][n] for m in range (3 * i, 3 * i + 3)for n in range(3 * j, 3*j + 3)]):
                    return False
        return True    
    
    
    #判断是否是有效的list，去掉. 之后，set可以过滤相同的元素，过滤之后，看len是否相等
    def isValidList(self, xs):
        xs = list(filter(lambda x: x != '.', xs))
        return len(set(xs)) == len(xs)
    
    
    
if __name__ == "__main__":
    board = [[5, '.', '.', '.', '.', '.', '.', '.', '.'],
             [5, 2, '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', 3, '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', 4, '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', 5, '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', 6, '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', 7, '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', 8, '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.', 9]]
    print(Solution().isValidSudoku(board))
    
    
    
    