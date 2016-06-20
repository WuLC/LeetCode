# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-06-20 23:14:57
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-20 23:15:29
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        words.reverse()
        return ' '.join(words)