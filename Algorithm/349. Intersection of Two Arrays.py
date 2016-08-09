# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-08-09 22:04:52
# @Last modified by:   WuLC
# @Last Modified time: 2016-08-09 23:26:43
# @Email: liangchaowu5@gmail.com

# transfer the two lists to two sets, and find their intersection set
 

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        nums1, nums2 = set(nums1), set(nums2)
        for num in nums2:
            if num in nums1:
                result.append(num)
        return result

# similar to the above code , use built_in intersection of two sets
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        s1, s2 = set(nums1), set(nums2)
        return list(s1&s2)