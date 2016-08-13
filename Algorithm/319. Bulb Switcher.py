# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-13 21:27:15
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-13 21:27:21
# @Email: liangchaowu5@gmail.com
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        count, num = 0, 1
        while pow(num, 2) <= n:
            count += 1
            num += 1
        return count