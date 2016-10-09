# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-06 15:21:07
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-06 16:09:43
# @Email: liangchaowu5@gmail.com

# find the longest prefix palindromic string of the original string  

# O(n^2), TLE
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        prefix = []
        for i in reversed(xrange(len(s))):
            if s[i] == s[0]:
                if self.is_palindrome(s[:i+1]):
                    return ''.join(prefix)+s
            prefix.append(s[i])
    
    def is_palindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

# Base on KMP, build the Partial match table
# https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm#.22Partial_match.22_table_.28also_known_as_.22failure_function.22.29
# O(n) time, O(n) space, AC
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
            return s
        reverse_str = s[::-1]
        mix = s + '#' + reverse_str
        t = [0 for i in xrange(len(mix))]
        for i in xrange(1, len(mix)):
            j = t[i-1]
            while j > 0 and mix[i] != mix[j]:
                j = t[j-1]
            t[i] = j + 1 if mix[j] == mix[i] else j
        return reverse_str[:len(s)-t[-1]] + s