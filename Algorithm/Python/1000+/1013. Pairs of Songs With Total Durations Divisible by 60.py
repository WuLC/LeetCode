# -*- coding: utf-8 -*-
# Created on Wed Mar 20 2019 21:8:13
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# O(n) time, hashmap


class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        result, count = 0, [0]*60
        for t in time:
            result += count[(60-(t % 60)) % 60]
            count[t % 60] += 1
        return result


# faster solution

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        count = [0] * 60
        for t in time:
            count[t % 60] += 1
        result = 0
        for i in xrange(31):
            if i == 0 or i == 30:
                result += (count[i] * (count[i] - 1)) >> 1
            else:
                result += count[i] * count[60 - i]
        return result
