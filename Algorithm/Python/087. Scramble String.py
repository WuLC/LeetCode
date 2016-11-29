# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-11-29 17:58:53
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-29 19:48:39
# @Email: liangchaowu5@gmail.com

# recursive


# stupid recursive, TLE and MLE
from collections import Counter
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2) or Counter(s1) != Counter(s2):
            return False
        return s2 in self.helper(s1)

    def helper(self, s):
        """return all possible scramble strings of s"""
        n = len(s)
        if n < 2:
            return {s}
        scramble_strings = set()
        for i in xrange(1, n):
            set1 = self.helper(s[:i])
            set2 = self.helper(s[i:])
            for s1 in set1:
                for s2 in set2:
                    scramble_strings.add(s1+s2)
                    scramble_strings.add(s2+s1)
        return scramble_strings


# modified recursive method, 125ms
from collections import Counter
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2) or Counter(s1) != Counter(s2):
            return False
        if s1 == s2:
            return True
        n = len(s1)
        for i in xrange(1, n):
            if (self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:])) or (self.isScramble(s1[:i],s2[n-i:]) and self.isScramble(s1[i:],s2[:n-i])):
                return True
        return False
            
            
            