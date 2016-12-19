# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-12-19 17:44:48
# @Last modified by:   WuLC
# @Last Modified time: 2016-12-19 19:43:49
# @Email: liangchaowu5@gmail.com



# naive solution and deal with duplicate numbers
# still TLE
from collections import Counter
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        result = 0
        sorted_nums = sorted(list(set(nums)))
        for i in xrange(len(sorted_nums)):
            for j in xrange(i+1, len(sorted_nums)):
                tmp = sorted_nums[i] ^ sorted_nums[j]
                curr_distance = 0
                for k in xrange(31):
                    curr_distance += (1&(tmp>>k))
                result += curr_distance * count[sorted_nums[i]] * count[sorted_nums[j]]
        return result
                
                
# count bit by bit, 
# the distance provided by each bit is the number of 0 at this bit multiplied by the number of 1 at this bit
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in xrange(31):
            one, zero = 0, 0
            for num in nums:
                if (num>>i) & 1:
                    one += 1
                else:
                    zero += 1
            result += one*zero
        return result
        