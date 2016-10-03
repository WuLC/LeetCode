# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-10-03 20:02:50
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-03 20:03:09
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        for char in s:
            count.setdefault(char, 0)
            count[char] += 1
        result, odd = 0, False
        for length in count.values():
            if length % 2 == 0:
                result += length
            else:
                result += (length - 1)
                odd = True
        return result+1 if odd else result
    
        
                
            