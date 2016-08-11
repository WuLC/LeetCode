# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-11 09:40:13
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-11 09:40:19
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count = 0
        while count < 32:
            if n & 1 == 1:
                if n >> 1 == 0:
                    return True
                else:
                    return False
            count += 1
            n >>= 1
        return False