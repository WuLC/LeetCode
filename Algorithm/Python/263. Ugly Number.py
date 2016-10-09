# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-11 08:23:30
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-11 08:23:39
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0: 
            return False
        while num % 2 == 0:
            num /= 2
        while num %3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5
        if num == 1:
            return True
        else:
            return False