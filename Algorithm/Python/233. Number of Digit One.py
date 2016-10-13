# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-10-13 22:53:34
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-14 00:08:01
# @Email: liangchaowu5@gmail.com

# find out how many times 1 appears at each bit
# at each bit, discuss the following three case: 0, 1 and >=1
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        s = str(n)
        m, count = len(s), 0
        for i in xrange(m):
             high = int(s[:i]) if i!=0 else 0
             low = int(s[i+1:]) if i!= m-1 else 0
             bit = m-1-i
             if s[i] == '0':
                 count += high * pow(10, bit)
             elif s[i] == '1':
                 count += (high * pow(10, bit) + low + 1)
             else:
                 count += (high+1)*pow(10, bit)
        return count