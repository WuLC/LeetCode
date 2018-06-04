# -*- coding: utf-8 -*-
# Created on Mon Jun 04 2018 20:25:29
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# simple solution 
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def backspace_str(s):
            tmp = []
            for c in s:
                if c == '#':
                    if len(tmp) > 0:
                        tmp.pop()
                else:
                    tmp.append(c)
            return ''.join(tmp)
        return backspace_str(S) == backspace_str(T)