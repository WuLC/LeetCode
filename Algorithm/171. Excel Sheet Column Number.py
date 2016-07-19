# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-19 14:34:39
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-19 14:34:59
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, n = 0, len(s)
        for i in xrange(n):
            result += (ord(s[i])-64)*pow(26, n-i-1)
        return result
            