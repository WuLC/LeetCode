# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-02-10 11:11:15
# @Last modified by:   WuLC
# @Last Modified time: 2017-02-10 11:11:34
# @Email: liangchaowu5@gmail.com


# recursive method , AC
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.firstWin(0, 0, nums, 0, len(nums)-1)
    
    def firstWin(self, s1, s2, nums, start, end):
        """return true if the first person to pick the number finally win"""
        if start > end:
            return True if s1>=s2 else False
        return not (self.secondWin(s1+nums[start], s2, nums, start+1, end) and self.secondWin(s1+nums[end], s2, nums, start, end-1))
        
    def secondWin(self, s1, s2, nums, start, end):
        """return true if the second person to pick the number finally win"""
        if start > end:
            return True if s1 < s2 else False
        return not (self.firstWin(s1, s2+nums[start], nums, start+1, end) and self.firstWin(s1, s2+nums[end], nums, start, end-1))