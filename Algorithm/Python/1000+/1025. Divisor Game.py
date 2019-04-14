# -*- coding: utf-8 -*-
# Created on Sun Apr 14 2019 12:43:40
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# anyone starting with odd number will lose
class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return N % 2 == 0