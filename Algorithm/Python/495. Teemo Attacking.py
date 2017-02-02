# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-02-02 13:24:13
# @Last modified by:   WuLC
# @Last Modified time: 2017-02-02 15:36:28
# @Email: liangchaowu5@gmail.com


# O(n) time, find the time point that each poisoned condition end
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        result = 0
        endPoint = 0
        for num in timeSeries:
            poisonedTime = duration if num>= endPoint else (num+duration-endPoint)
            result +=  poisonedTime
            endPoint = num+duration
        return result
            