# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-06-25 16:14:24
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-25 21:53:30
# @Email: liangchaowu5@gmail.com

# method 1 ,find the valid string firstly, then judge whether isPalindrome, TLE
# O(n), traverse twice
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = ''
        for i in xrange(len(s)):
            if 'a'<=s[i]<='z' or 'A'<=s[i]<='Z' or '0'<= s[i] <= '9':
                st += s[i]
        n = len(st)
        for i in xrange(n/2):
            a, b = ord(st[i]), ord(st[n-i-1])
            if a == b :
                continue
            elif a >= 65 and  b >= 65 and abs( a-b ) == 32:
                continue
            else:
                return False
        return True


# method2, Two Pointers, AC
# O(n), traverse just once
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not self.isValid(s[left]):
                left += 1
            while left < right and not self.isValid(s[right]):
                right -= 1
            if left < right:
                a, b = ord(s[left]), ord(s[right])
                if s[left] == s[right] or abs(a - b)==32 and a >= 65 and b >= 65:
                    left += 1
                    right -= 1
                    continue
                else:
                    return False
        return True
        
    def isValid(self, char):
        return 'a'<=char<='z' or 'A'<=char<='Z' or '0'<=char<='9'