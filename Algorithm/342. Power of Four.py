# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-11 09:40:30
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-11 09:40:38
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        count = 0
        while count < 32:
            if num & 1 == 1:
                if num >> 1 == 0 and count %2 == 0:
                    return True
                else:
                    return False
            count += 1
            num >>= 1
        return False