# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-03-30 17:29:05
# @Last Modified by:   WuLC
# @Last Modified time: 2017-03-30 17:40:19


# split the complex number into two part and caculate the real part and the imaginary part respectively
class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ar, av = map(lambda x: int(x), a[:-1].split('+'))
        br, bv = map(lambda x: int(x), b[:-1].split('+'))
        r = ar*br - av*bv
        v = ar*bv + br*av
        return '%s+%si'%(r,v)
        
        
        