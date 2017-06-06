# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-06-06 21:47:07
# @Last modified by:   WuLC
# @Last Modified time: 2017-06-06 22:17:02
# @Email: liangchaowu5@gmail.com


# naive O(n^2), TLE
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in xrange(1, len(nums)):
            nums[i] += nums[i-1]
        count = 0
        nums = [0] + nums
        for i in xrange(len(nums)-1):
            for j in xrange(i+1, len(nums)):
                if nums[j] - nums[i] == k:
                    count += 1
        return count


# O(n), hashmap 
# referer: https://discuss.leetcode.com/topic/87866/python-simple-with-explanation
from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        count = defaultdict(int)
        count[0] = 1
        result = 0
        accu = 0
        for num in nums:
            accu += num
            result += count[accu - k]
            count[accu] += 1
        return result