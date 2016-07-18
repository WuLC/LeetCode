# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-18 09:42:04
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-18 09:42:48
# @Email: liangchaowu5@gmail.com

# backtracking
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        self.helper(s, 0, [], result)
        return result
        
    def helper(self, s, idx, tmp, result):
        if idx == len(s):
            result.append(tmp[:])
            return
        for i in xrange(idx+1, len(s)+1):
            t = s[idx:i]
            if self.is_palindrome(t):
                tmp.append(t)
                self.helper(s, i, tmp, result)
                tmp.pop()
            
    def is_palindrome(self, s):
        n = len(s)
        for i in xrange(n/2):
            if s[i] != s[n-i-1]:
                return False
        return True