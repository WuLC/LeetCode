# -*- coding: utf-8 -*-
# Created on Tue Oct 30 2018 20:14:35
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# record prefix sum，applicable to any number
from collections import defaultdict
class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        count = defaultdict(int)
        count[0] = 1
        result, curr_sum = 0, 0
        for num in A:
            curr_sum += num
            result += count[curr_sum - S]
            count[curr_sum] += 1
        return result