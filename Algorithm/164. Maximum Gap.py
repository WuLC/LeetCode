# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-12 22:39:31
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-12 22:39:37
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return 0
        MAX_INT, MIN_INT = sys.maxint, -sys.maxint-1
        n, result = len(nums), 0
        max_bucket = [MIN_INT for i in xrange(n-1)]
        min_bucket = [MAX_INT for i in xrange(n-1)]
        min_num, max_num = min(nums), max(nums)
        gap = int(math.ceil((float)(max_num - min_num)/(n-1)))
        for num in nums:
            if num == min_num or num == max_num:
                continue
            bucket = int((num - min_num)/gap)
            max_bucket[bucket] = max(max_bucket[bucket], num)
            min_bucket[bucket] = min(min_bucket[bucket], num)
        previous = min_num
        for i in xrange(n-1):
            if max_bucket[i]==MIN_INT:
                continue
            result = max(result, min_bucket[i]-previous)
            previous = max_bucket[i]
        result = max(result, max_num - previous)
        return result
            
            