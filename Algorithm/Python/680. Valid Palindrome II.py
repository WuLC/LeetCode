# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-09-20 11:10:06
# @Last Modified by:   WuLC
# @Last Modified time: 2017-09-20 12:39:07


# the following method will lead to maximum recursion exceed with large input
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self.isPalindrome(s, 0, len(s) - 1, 0)
    
    def isPalindrome(self, s, start, end, count):
        if s[start] == s[end]:
            if start == end or start + 1 == end:
                return True
            else:
                return self.isPalindrome(s, start + 1, end - 1, count) 
        else:
            if count == 1:
                return False
            return self.isPalindrome(s, start + 1, end, count + 1) or self.isPalindrome(s, start, end - 1, count + 1) 


# same method above, but drop the recursive pattern
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start, end = 0, len(s) - 1
        while start <= end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return self.isPalindrome(s, start, end-1) or self.isPalindrome(s, start + 1, end)
        return True
    
    def isPalindrome(self, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True