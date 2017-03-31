# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-03-31 23:48:21
# @Last modified by:   WuLC
# @Last Modified time: 2017-03-31 23:49:23
# @Email: liangchaowu5@gmail.com

# naive solution
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1: return False
        tmp = 1
        for i in xrange(2, int(math.sqrt(num))+1):
            if num % i == 0:
               tmp += (i + num/i)
        return tmp == num