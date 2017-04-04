# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-04 20:58:06
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-04 21:01:11
# @Email: liangchaowu5@gmail.com


# don't think over it
# when length is not equal, just return the longest
# when length is equal and two strings are different, still return their length

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        return -1 if a == b else max(len(a), len(b))