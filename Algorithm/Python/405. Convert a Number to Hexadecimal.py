# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-26 23:13:42
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-26 23:13:49
# @Email: liangchaowu5@gmail.com


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        result, count, tmp  = '', 0, 0
        for i in xrange(32):
            tmp += (num & (1<<i))
            count += 1
            if count % 4 == 0:
                tmp >>= (count-4)
                char = chr(97 + tmp - 10) if tmp >= 10 else str(tmp)
                tmp = 0
                result = char + result
        return result.lstrip('0') or '0'
        