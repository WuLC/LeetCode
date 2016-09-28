# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-09-27 23:58:09
# @Last modified by:   WuLC
# @Last Modified time: 2016-09-28 23:04:12
# @Email: liangchaowu5@gmail.com

# stack
# sort the people in ascending order for the first element and descending order for the second element
# then pop the popple and insert them to the index which is the same as  the second elemnt
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        def compare(x, y):
            if  x[0] != y[0]:
                return x[0] - y[0]
            else:
                return y[1] - x[1]
        
        result = []
        people.sort(cmp = compare)
        while people:
            tmp = people.pop()
            result.insert(tmp[1],tmp)
        return result
        
        