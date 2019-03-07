# -*- coding: utf-8 -*-
# Created on Thu Mar 07 2019 20:36:25
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# binary search

from collections import defaultdict
from bisect import bisect_left

class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.db = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.db[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.db:
            return ""
        # custom binary search
        # idx = self.binary_search(key, timestamp)
        # built-in binary search
        idx = bisect_left(self.db[key], (timestamp, '{')) # use '{' because its ascii code is larger than lowercase letter
        return self.db[key][idx-1][1] if idx != 0 else ""

    def binary_search(self, key, timestamp):
        left, right = 0, len(self.db[key]) - 1
        while left < right:
            mid = left + ((right-left)>>1)
            if self.db[key][mid][0] == timestamp:
                break
            elif self.db[key][mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        return left if self.db[key][left][0] <= timestamp else left-1



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)