# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-20 14:12:46
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-20 14:12:57
# @Email: liangchaowu5@gmail.com


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        count, base = 0, 1
        while (count + base * 9 * pow(10, base -1)) < n:
            count += base * 9 * pow(10, base -1)
            base += 1
        left = n - count
        num, mod = divmod(left, base)
        if mod:
            return int(str(pow(10,base-1) + num)[mod-1])
        else:
            return int(str(pow(10,base-1) + num -1)[mod-1])