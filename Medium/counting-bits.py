#-*- coding:utf-8 -*-
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res_list = []
        for i in range(num + 1):
            str_num = bin(i)
            len_str_num = len(str_num)
            real_str_num = str_num[2:len_str_num]
            #test:print(real_str_num)
            len_real_str_num = len(real_str_num)
            count = 0
            for j in range(len_real_str_num):
                if real_str_num[j] == '1':
                    count += 1
            res_list.append(count)
        return res_list

if __name__ == "__main__":
    print(Solution().countBits(2))
