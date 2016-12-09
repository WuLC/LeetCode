# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-22 22:26:24
# @Last modified by:   WuLC
# @Last Modified time: 2016-12-09 19:00:54
# @Email: liangchaowu5@gmail.com

# method 1, bit manipulation
# if A = B^c , then c = A^B
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = len(nums)
        for i in xrange(len(nums)):
            result ^= i
            result ^= nums[i]
        return result
        # one-line solution of the above code
        # return reduce(lambda x,y:x^y, xrange(len(nums)+1))^reduce(lambda x,y:x^y, nums)
        

# method 2, sum
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, total = 0, 0
        for i in xrange(len(nums)):
            count += nums[i]
            total += i
        total += len(nums)
        return total - count