#-*- coding:utf-8 -*-

#是否是有效括号的判断：
#The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not
#首先，想到的是每一对括号都要是分拆后都要是偶数个。其次每次出现都要按照一定的次序成对出现。

#算法思想：用dict
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        