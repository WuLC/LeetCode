# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-11-20 21:16:52
# @Last modified by:   WuLC
# @Last Modified time: 2016-11-20 21:18:12
# @Email: liangchaowu5@gmail.com

# O(n^2) solution is naive
# with bit-by-bit manipulation make the time complexity O(n)
# referer: https://discuss.leetcode.com/topic/63213/java-o-n-solution-using-bit-manipulation-and-hashmap/7
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, mask = 0, 0
        for i in reversed(xrange(32)):
            mask = mask | (1<<i)
            prefixs = {num & mask for num in nums}
            tmp = result | (1<<i)
            for prefix in prefixs:
                if prefix ^ tmp in prefixs:
                    result = tmp
                    break
        return result