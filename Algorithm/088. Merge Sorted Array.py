# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-05-27 17:43:35
# @Last modified by:   WuLC
# @Last Modified time: 2016-05-27 17:46:33
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        index, i = 0, None
        while len(nums1) > m:
            nums1.pop()
        while len(nums2) > n:
            nums2.pop()
        for i in xrange(n):
            flag = 0  # mark whether the element nums2[i] is already inserted
            while index<len(nums1):
                if nums1[index] >= nums2[i]:
                    nums1.insert(index,nums2[i])
                    flag = 1
                    break
                else:
                    index += 1
            if index == len(nums1):
                break
        if i!=None:
            if flag==0:
                nums1 += nums2[i:] 
            else:
                nums1 += nums2[i+1:]
            
        