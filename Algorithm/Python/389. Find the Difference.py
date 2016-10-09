# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-08-30 20:33:00
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-30 20:42:17
# @Email: liangchaowu5@gmail.com

# hash table
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        mapping = {}
        for char in s:
            mapping.setdefault(char, 0)
            mapping[char] += 1
        for char in t:
            if char not in mapping or mapping[char] == 0:
                return char
            mapping[char] -= 1



# bit manipulation
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = 0
        for char in s+t:
            offset = ord(char)-97
            count ^= (1 << offset)
        result = 0
        while count!=1:
            count >>= 1
            result += 1
        return chr(97+result)