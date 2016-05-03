#-*-coding:utf-8-*-
class Solution(object):
    def lengthOfLastWord(self, s):
       #这里用到strip(rm)函数，strip可以删除s开头和结尾的rm，若为空，默认删除开头和结尾的空白字符
       return len(s.strip().split(" ")[-1])
if __name__ == "__main__":
    
    print(Solution().lengthOfLastWord(""))