# -*- coding:utf-8 -*-
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_list = list(a)
        b_list = list(b)
        len_a = len(a_list)
        len_b = len(b_list)
        if len_a < len_b:
            length = len_b - len_a
            for i in range(length):
                a_list.insert(0, '0')
        else:
            length = len_a - len_b
            for i in range(length):
                b_list.insert(0, '0')
        #print("a %s" % a_list)
        #print("b %s" % b_list)
        real_len = len(a_list)
        result = []
        jw = 0
        for i in range(real_len):
            sum = int(a_list[real_len - i - 1]) + int(b_list[real_len - i - 1]) + jw
            
            if sum == 2:
                #产生进位
                result.append('0')
                jw = 1
                #print(result)
            elif sum == 0:
                result.append('0')
                jw = 0
                #print(result)
            elif sum == 3:
                result.append('1')
                jw = 1
            else:
                result.append('1')
                jw = 0
                #print(result)
        result.reverse()
        if jw == 1:
            result.insert(0, '1')
        res_str = "".join(result)
        return res_str

if __name__ == "__main__":
    print(Solution().addBinary("1111", "1111"))
                    
                