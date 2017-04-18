# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-04-18 12:46:58
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-18 12:47:06
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(map(lambda x:x[::-1], s.split()))