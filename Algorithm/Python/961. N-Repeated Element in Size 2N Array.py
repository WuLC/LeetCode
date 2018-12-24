# -*- coding: utf-8 -*-
# Created on Mon Dec 24 2018 13:47:29
# Author: WuLC
# EMail: liangchaowu5@gmail.com

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        appeared = set()
        for num in A:
            if num in appeared:
                return num
            appeared.add(num)
        return -1