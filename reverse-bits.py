#-*- coding:utf-8 -*-
#1)进制的相互转换：十进制<=>二进制
#2）类型的相互转换：string<=>list
class Solution(object):
    def reverseBits(self, n):
        #十进制转换为二进制
        string = bin(n)
        length = len(string)
        real_string = string[2:length]
        real_len = length - 2
        strlist = list(real_string)
        #初始化list
        new_strlist = ['0'] * 32
        #reverse strlist
        for i in range(real_len):
            new_strlist[i] = strlist[real_len - i - 1]
        #list to str
        reverse_str = "".join(new_strlist)
        #二进制转换为十进制
        result = int(reverse_str, 2)
        return result

if __name__ == "__main__":
    print(Solution().reverseBits(43261596))