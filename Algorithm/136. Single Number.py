# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-07-15 09:28:08
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-15 10:42:04
# @Email: liangchaowu5@gmail.com

# method 1, use set, O(n) space
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = set()
        for i in xrange(len(nums)):
            if nums[i] in count:
                count.remove(nums[i])
            else:
                count.add(nums[i])
        return count.pop()

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2*sum(set(nums)) - sum(nums)


# method 2, use dict, O(n) space
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for i in xrange(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        for k,v in count.items():
            if v == 1:
                return k

# method 3,xor, O(1) space
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x,y: x^y, nums)
            