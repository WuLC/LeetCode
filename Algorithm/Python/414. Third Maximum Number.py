# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-10-23 14:38:40
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-23 14:38:54
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_nums = set()
        for num in nums:
            if len(max_nums) < 3:
                max_nums.add(num)
            else:
                min_num = min(max_nums)
                if min_num < num and num not in max_nums:
                    max_nums.remove(min_num)
                    max_nums.add(num)
        return max(max_nums) if len(max_nums)<3 else min(max_nums)