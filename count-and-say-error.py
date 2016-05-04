# -*-coding:utf-8 -*-
#读题错误，要求是连续的1如果重复的时候，进行计数，统计个数
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        n_str = str(n)
        n_list = list(n_str)
        #不同的元素数
        n_set = set(n_list)
        len_n_set = len(n_set)
        print(n_set)
        print(n_list)
        #n_dict用来存储key-value，其中key是不同元素数，value是count
        n_dict = dict()
        for i in range(len_n_set):
            count = 0
            for e in n_list:
                if e == list(n_set)[i]:
                    count += 1
                    n_dict[list(n_set)[i]] = count
        print(n_dict)
        res_str = ''
        for key,value in n_dict.items():
            res_str += str(value)
            res_str += str(key)
        return res_str


if __name__ == "__main__":
    num = 1
    for i in range(1,6):
        if i == 1:
            print('1')
        else:
            print(Solution().countAndSay(num))
            num = int(Solution().countAndSay(num))
    
        
            