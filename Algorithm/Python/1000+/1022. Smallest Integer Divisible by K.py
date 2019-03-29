# -*- coding: utf-8 -*-
# Created on Sun Mar 24 2019 22:28:18
# Author: WuLC
# EMail: liangchaowu5@gmail.com

class Solution(object):
    def smallestRepunitDivByK(self, K):
        """
        :type K: int
        :rtype: int
        """
        if 1 % K == 0:
            return 1
        elif 11 % K == 0:
            return 2
        elif 111 % K == 0:
            
