#-*-coding:utf-8-*-

#这种方法太傻了。。。
from math import floor
class Solution(object):
    def convertToTitle(self, n):
        lookup = {0:'Z',1:'A', 2:'B', 3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z' }
        #lookup = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26 }
        if n <= 26:
            return lookup[n] 
        else:
            w = floor((n-1) / 26)
            #test:print(w)
            res_str = ''
            v = n % 26
            org_str = lookup[v]
            #test:print(v)
            while w > 26:
                v = w % 26
                w = floor((w - 1)/ 26)
                #test:print(w)
                #test:print(v)
                res_str += lookup[v]
            #test:print(w)
            if w <= 26 :
                w_str = lookup[w]
#             elif w <= 26 and v == 0:
#                 w_str = lookup[w-1]
            
            #test:print(org_str + res_str + w_str)
            res_list = list(org_str + res_str + w_str)
            #test:print(res_list)
            res_list.reverse()
            return ''.join(res_list)
if __name__ == "__main__":
    print(Solution().convertToTitle(702))  