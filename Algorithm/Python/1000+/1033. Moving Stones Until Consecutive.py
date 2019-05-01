# -*- coding: utf-8 -*-
# Created on Wed May 01 2019 17:25:35
# Author: WuLC
# EMail: liangchaowu5@gmail.com

class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        nums = sorted([a, b, c])
        min_move = min(1, nums[1]-nums[0]-1) + min(1, nums[2]-nums[1]-1)
        # for the case like 1 3 5
        if nums[2] - nums[1] == 2 or nums[1] - nums[0] == 2:
            min_move = min(min_move, 1)
        max_move = nums[2] - nums[0] - 2
        return [min_move, max_move]
