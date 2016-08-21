# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-21 13:22:00
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-21 13:22:08
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4 != 0