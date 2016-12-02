# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-12-02 21:02:49
# @Last modified by:   WuLC
# @Last Modified time: 2016-12-02 21:06:36
# @Email: liangchaowu5@gmail.com

# referer: https://discuss.leetcode.com/topic/35494/solution-explanation
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        edge, miss = 1, 0
        for num in nums:
            while edge <= n and edge < num: # n can be smaller than num
                edge <<= 1
                miss += 1
            edge += num
            if edge > n:
                return miss
        while edge <= n:
            edge <<= 1
            miss += 1
        return miss