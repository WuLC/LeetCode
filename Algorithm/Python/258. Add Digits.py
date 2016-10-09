# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-25 10:50:43
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-25 10:51:36
# @Email: liangchaowu5@gmail.com


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else: 
            return num % 9