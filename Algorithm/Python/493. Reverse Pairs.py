# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-03-12 23:19:58
# @Last modified by:   WuLC
# @Last Modified time: 2017-03-12 23:30:29
# @Email: liangchaowu5@gmail.com


# merge sort, time O(nlogn)
# referer:https://discuss.leetcode.com/topic/78933/very-short-and-clear-mergesort-bst-java-solutions
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.merge_sort(nums, 0, len(nums)-1)
        
    def merge_sort(self, nums, start, end):
        if start >= end: 
            return 0
        mid = start + ((end - start)>>1)
        count = self.merge_sort(nums, start, mid) + self.merge_sort(nums, mid+1, end)
        # count reverse pairs for current two sorted array
        j = mid + 1
        for i in xrange(start, mid+1):
            while j <= end and nums[i] > nums[j]*2:
                j += 1
            count += (j - mid - 1)
            
        # merge two sorted array
        left, right = nums[start:mid+1], nums[mid+1:end+1]
        idx = start
        p1, p2 = 0, 0
        while p1 < len(left) or p2 < len(right):
            if p1 < len(left) and (p2 == len(right) or left[p1] < right[p2]):
                nums[idx] = left[p1]
                p1 += 1
            else:
                nums[idx] = right[p2]
                p2 += 1
            idx += 1
        return count
        