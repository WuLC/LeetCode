# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-12-20 21:04:25
# @Last modified by:   WuLC
# @Last Modified time: 2016-12-20 21:05:12
# @Email: liangchaowu5@gmail.com



# binary search, find the closest heater for each house
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        distance = 0
        for house in houses:
            distance = max(distance, self.binary_search(heaters, house))
        return distance
        
        
    def binary_search(self, heaters, house):
        left, right = 0, len(heaters) - 1
        while left < right:
            mid = left + ((right - left)>>1)
            if heaters[mid] == house:
                return 0
            elif heaters[mid] > house:
                right = mid
            else:
                left = mid + 1
        if heaters[left] == house:
            return 0
        elif heaters[left] > house:
            return heaters[left] - house if left == 0 else min(heaters[left] - house, house - heaters[left-1])
        else:
            return house - heaters[left] if left == len(heaters)-1 else  min(house - heaters[left],  heaters[left+1] - house)
            