# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-05-08 08:36:52
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-08 08:37:02
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = s.split()
        if len(result) == 0:
            return 0
        else:
            return len(result[-1])
        