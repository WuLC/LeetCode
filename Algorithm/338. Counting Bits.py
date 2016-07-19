# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-07-19 15:19:08
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-19 15:19:21
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0 for i in xrange(num+1)]
        for i in xrange(1, num+1):
            result[i] = result[i>>1] + (i&1)
        return result