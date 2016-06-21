# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-21 13:08:24
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-21 13:11:16
# @Email: liangchaowu5@gmail.com


# method 1 ,sort firstly,O(nlogn)
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in xrange(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
     
# methond 2, use set instead of list,O(n)
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for i in xrange(len(nums)):
            if nums[i] in s:
                return True
            else:
                s.add(nums[i])
        return False
        