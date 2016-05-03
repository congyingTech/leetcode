#-*- coding:utf-8 -*-

#是否是有效括号的判断：
#The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not
#首先，想到的是每一对括号都要是分拆后都要是偶数个。其次每次出现都要按照一定的次序成对出现。

#算法思想：用dict，每一个括号相互匹配，进出栈的问题。
class Solution(object):
    def isValid(self, s):
        #list的初始化， stack = []
        stack, lookup = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in s:
            if parenthese in lookup:
                stack.append(parenthese)
                
            #1)stack 的 len为0的时候，说明这个字串中并不是括号，所以return False
            #2)stack里面存的是左括号，出栈的时候（左括号出栈），dict[key] = value 推知，lookup[stack.pop()]得到右括号
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
                return False
        #当stack都能够pop完，len为0的时候说明是正确的。
        return len(stack) == 0


if __name__ == "__main__":
    print(Solution().isValid("([{]})"))
