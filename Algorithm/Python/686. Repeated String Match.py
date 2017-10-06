# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-10-06 22:38:38
# @Last Modified by:   WuLC
# @Last Modified time: 2017-10-06 22:42:01


# try three possibilities, slow
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        count = len(B)/len(A)
        if self.isSubstring(A * count, B):
            return count
        elif self.isSubstring(A * (count + 1), B):
            return count + 1
        elif self.isSubstring(A * (count + 2), B):
            return count + 2
        else:
            return -1
            
            
    
    def isSubstring(self, s1, s2):
        """judge whether s2 is substring of s1"""
        if len(s2) == 0:
            return False
        for i in xrange(len(s1) - len(s2) + 1):
            if s1[i] == s2[0] and i + len(s2) <= len(s1) and s1[i: i + len(s2)] == s2:
                return True
        return False