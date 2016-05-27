# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-05-27 16:09:44
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-27 16:10:19
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return map(lambda x:x^(x>>1), range(pow(2,n))) # or change pow(2,n) to 1<<n
        