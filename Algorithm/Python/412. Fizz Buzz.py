# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-10-15 16:23:38
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-15 16:24:26
# @Email: liangchaowu5@gmail.com


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in xrange(1, n+1):
            tmp = ''
            if i%3 == 0:
                tmp += 'Fizz'
            if i%5 == 0:
                tmp += 'Buzz'
            if len(tmp) == 0:
                tmp = str(i)
            result.append(tmp)
        return result