# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-02-08 20:27:23
# @Last modified by:   WuLC
# @Last Modified time: 2017-02-08 20:37:24
# @Email: liangchaowu5@gmail.com

# naive solution, O(mn), AC
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for findNum in findNums:
            tmp = -1
            find = False
            for i in xrange(len(nums)):
                if findNum == nums[i]:
                    find = True
                if find and nums[i] > findNum:
                    tmp = nums[i]
                    break
            result.append(tmp)
        return result
                    