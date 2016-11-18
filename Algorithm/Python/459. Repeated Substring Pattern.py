# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-11-18 23:42:21
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-18 23:42:45
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        for i in xrange(1, len(str)):
            if str[i]==str[0] and len(str) % i == 0 and str[:i]*(len(str)/i) == str:
                return True
        return False