# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-12 14:17:13
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-12 14:17:21
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        index,reach = 0, 0 
        while index<=reach and index<len(nums):
            reach = max(reach, index+nums[index])
            index += 1
        if reach >= len(nums)-1:
            return True
        else:
            return False