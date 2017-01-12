# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-01-12 14:30:02
# @Last modified by:   WuLC
# @Last Modified time: 2017-01-12 14:32:50
# @Email: liangchaowu5@gmail.com

# get each bit except the leading zeros, then reverse it and xor with the result
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        count, result = 0, 0
        tmp = num
        while tmp > 0:
            tmp >>= 1
            count += 1
        # get each bit and reverse it
        for i in xrange(count):
            bit = (1<<i) & num
            bit ^= (1<<i) # reverse it 
            result ^= bit
        return result
        
        