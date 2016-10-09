# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-09 21:19:19
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-09 21:20:41
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        index, result = 0, []
        previous, start = nums[0], nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] - previous == 1:
                previous = nums[i]
            else:
                if previous != start:
                    result.append("%s->%s"%(start, previous))
                else:
                    result.append(str(start))
                previous, start = nums[i], nums[i]
        # deal with the last range
        if previous != start:
            result.append("%s->%s"%(start, previous))
        else:
            result.append(str(start))
        return result