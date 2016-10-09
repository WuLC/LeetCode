# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-09 20:28:47
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-09 20:28:59
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        pairs = []
        for i in xrange(len(nums1)):
            for j in xrange(len(nums2)):
                pairs.append([nums1[i], nums2[j]])
        return heapq.nsmallest(k, pairs, key = sum)