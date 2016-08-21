# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-21 13:22:00
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-21 14:33:19
# @Email: liangchaowu5@gmail.com

# The first one who got the number that is multiple of 4 (i.e. n % 4== 0) will lost, otherwise he/she will win
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n%4 != 0