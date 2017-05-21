# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-05-21 14:31:21
# @Last modified by:   WuLC
# @Last Modified time: 2017-05-21 14:31:57
# @Email: liangchaowu5@gmail.com

# hash table,  count and sort 
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for num in nums:
            count.setdefault(num, 0)
            count[num] += 1
        sorted_count = sorted(count.items())
        
        result = 0
        for i in xrange(1, len(sorted_count)):
            if sorted_count[i][0] - sorted_count[i-1][0] == 1:
                result = max(result, sorted_count[i][1] + sorted_count[i-1][1])
        return result
                