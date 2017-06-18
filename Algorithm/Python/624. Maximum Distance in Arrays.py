# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-06-18 16:34:58
# @Last modified by:   LC
# @Last Modified time: 2017-06-18 16:38:28
# @Email: liangchaowu5@gmail.com


# O(n) time
# traverse the arrays, 
# keep the min number and max number among the traversed numbers so far and compare them with the current number

class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        result = 0
        curr_min, curr_max = arrays[0][0], arrays[0][-1]
        for i in xrange(1, len(arrays)):
            result = max(result, abs(arrays[i][0] - curr_max), abs(arrays[i][-1] - curr_min))
            curr_max = max(curr_max, arrays[i][-1])
            curr_min = min(curr_min, arrays[i][0])
        return result