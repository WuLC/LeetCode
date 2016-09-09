# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-09 21:06:33
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-09 21:06:40
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        index = 0
        for char in t:
            if s[index] == char:
                index += 1
            if index == len(s):
                return True
        return False
        