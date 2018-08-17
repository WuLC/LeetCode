# -*- coding: utf-8 -*-
# Created on Fri Aug 17 2018 10:30:14
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# greedy, always put two people with largest weight and smallest weight together
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        count = 0
        left, right = 0, len(people)-1
        while left <= right:
            if people[left] + people[right] < limit:
                left += 1
                right -= 1
            else:
                right -= 1
            count += 1
        return count