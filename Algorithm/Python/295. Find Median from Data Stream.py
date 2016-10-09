# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-09-25 22:18:04
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-25 22:18:50
# @Email: liangchaowu5@gmail.com


# bianry search and then insert, O(n^2), AC
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.length = 0
        
    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        left, right = 0, self.length-1
        mid = None
        while left <= right:
            mid = left + (right - left) / 2
            if self.nums[mid] > num:
                right = mid - 1
            elif self.nums[mid] < num:
                left = mid + 1
            else:
                break
        if mid != None:
            if self.nums[mid] >= num:
                pos = mid
            else:
                pos = mid + 1
            self.nums.insert(pos, num)
        else:
            self.nums.append(num)
        self.length += 1

        
    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.length % 2:
            return float(self.nums[self.length/2])
        else:
            return float(self.nums[self.length/2-1]+self.nums[self.length/2])/2