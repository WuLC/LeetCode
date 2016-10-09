# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-07-19 13:45:42
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-19 13:53:37
# @Email: liangchaowu5@gmail.com


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = []
        while n:
            tmp = n % 26
            if tmp == 0: 
                result.append('Z')
            else:
                result.append(chr(tmp+64))
            # the above five lines can be replaced by the following line
            # result.append(chr((n-1) % 26+65))
            n = (n-1)/26
        result.reverse()
        return ''.join(result)
        