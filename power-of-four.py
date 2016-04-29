# -*- coding:utf-8 -*-
#满足两个条件：1）二进制数的高位为1，其余为为0，； 2）二进制的位数为奇数
import re
from posixpath import realpath
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #先将十进制转换为二进制
        string = bin(num)
        #二进制数的长度
        length = len(string)
        #真正的字符串
        real_string = string[2:length]
        #真正的长度
        real_len = length - 2
        #string to list
        strlist = list(real_string)
        #最高位的数字
        gw = strlist[0]
        count = 0
        for e in strlist:
            if gw != '1':
                return False
            elif e == '0':
               count += 1

        if count == real_len - 1 and count % 2 == 0:
            return True
        else:
            return False     

if __name__ == "__main__":
    num = 16
    print(Solution().isPowerOfFour(num))
        
                
        
            