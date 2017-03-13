# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-03-13 12:10:09
# @Last Modified by:   WuLC
# @Last Modified time: 2017-03-13 12:13:32


# transform string time point to integer with minutes as measure 
# then sort and find the min difference between time points, pay attention that the first and last time point should also be caculated
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def str_2_int(time_point):
            hour, miniute = time_point.split(':')
            return int(hour)*60 + int(miniute)
            
        times = map(str_2_int, timePoints)
        times.sort()
        result = min(times[-1] - times[0], 60*24 - times[-1] + times[0])
        for i in xrange(1, len(times)):
            result = min(times[i] - times[i-1], result)
        return result