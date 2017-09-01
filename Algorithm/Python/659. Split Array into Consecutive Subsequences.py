# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-09-01 20:32:22
# @Last Modified by:   WuLC
# @Last Modified time: 2017-09-01 22:40:48


# greedy
# try in the following order
# 1. append number to existing sequence 
# 2. build a new sequence
# if both above not work, return False

from collections import Counter, defaultdict
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = Counter(nums)
        conse_count = defaultdict(int)
        for num in nums:
            if count[num] == 0:
                continue
            elif conse_count[num] > 0:
                conse_count[num] -= 1
                conse_count[num + 1] += 1
                count[num] -= 1
            elif count[num+1] > 0 and count[num+2] > 0:
                conse_count[num + 3] += 1
                count[num] -= 1
                count[num+1] -= 1
                count[num+2] -= 1
            else:
                return False
        return True
