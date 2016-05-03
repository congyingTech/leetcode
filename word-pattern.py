#-*-coding:utf-8 -*-
class Solution(object):
    def wordPattern(self, pattern, str):
        pattern_list = list(pattern)
        str_list = str.split(" ")
        if len(pattern_list) != len(str_list):
            return False
        lookup = dict()
        for i in range(len(pattern_list)):
            #如果i下标指向的元素没有在lookup里面，就add一下
            if pattern_list[i] not in lookup:
                lookup[pattern_list[i]] = str_list[i]
            #如果i下标指向的元素在lookup里面，就判断，key值对应的value是否与str_list的元素相同
            else:
                if str_list[i] != lookup[pattern_list[i]]:
                    return False
        #test lookup: print(lookup)
        key_set = set()
        value_set = set()
        for key,value in lookup.items():
            key_set.add(key) 
            value_set.add(value)
        
            
        #test: print(key_set)
        #test: print(value_set)
        if len(key_set) != len(value_set):
            return False
        
        return True
        
if __name__ == "__main__":
    print(Solution().wordPattern("abba", "cat cat cat cat"))

