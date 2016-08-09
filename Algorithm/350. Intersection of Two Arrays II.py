# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-09 22:06:22
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-09 23:00:30
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic1, dic2, result = {}, {}, []
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        for num in nums1:
            dic1.setdefault(num, 0)
            dic1[num] += 1
        for num in nums2:
            if num in dic1 and dic1[num]>0:
                result.append(num)
                dic1[num] -= 1
        return result