# -*-coding:utf-8 -*-
#算法思想：用map解决，将s和t的每个字符成映射的关系，如果
class Solution:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        return self.halfIsom(s, t) and self.halfIsom(t, s)
         
    
    def halfIsom(self, s, t):
        lookup = {}
        for i in range(len(s)):
            #这里的思想是如果s[i]没有在lookup里面，也就是没有重复元素的话，将s[i]-t[i]映射添加
            #如果有重复的元素，就看在lookup中s[i]作为key对应的value是否和当前的t[i]相同，若不同，则说明不同构
            if s[i] not in lookup:
                #建立映射关系s和t
                lookup[s[i]] = t[i]
            elif lookup[s[i]] != t[i]:
                return False
        print(lookup)
        return True

if __name__ == "__main__":
    s = "foot"
    t = "look"
    print(Solution().isIsomorphic(s, t))
    