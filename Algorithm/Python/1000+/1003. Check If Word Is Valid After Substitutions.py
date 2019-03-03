# -*- coding: utf-8 -*-
# Created on Sun Mar 03 2019 10:39:41
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# the number of each character appeared so far should satisify #a>#b>#c
# and finally there should be #a=#b=#c

from collections import defaultdict


class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        count = defaultdict(int)
        for c in S:
            count[c] += 1
            if not (count['a'] >= count['b'] >= count['c']):
                return False
        return False if count['a'] != count['b'] != count['c'] else True