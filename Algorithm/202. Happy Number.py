# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-07-05 07:50:00
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-05 07:50:35
# @Email: liangchaowu5@gmail.com


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        occured = set()
        while n != 1:
            total = 0
            for s in str(n):
                total += pow(int(s), 2)
            if total in occured:
                return False
            occured.add(total)
            n = total
        return True