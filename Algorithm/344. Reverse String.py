# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-10 22:12:47
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-10 22:19:04
# @Email: liangchaowu5@gmail.com

# method 1, AC
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = []
        for i in reversed(xrange(len(s))):
            chars.append(s[i])
        return ''.join(chars)

# method 2,TLE
# strings are immutable,so every time where it looks like you're appending a character onto your new_string
# it's theoretically creating a new string every time
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        for i in reversed(xrange(len(s))):
            result += s[i]
        return result


# method 3, easiest
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]