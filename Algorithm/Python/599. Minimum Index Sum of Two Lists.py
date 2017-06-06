# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-06-06 09:01:31
# @Last modified by:   WuLC
# @Last Modified time: 2017-06-06 09:01:46
# @Email: liangchaowu5@gmail.com


# hash table
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        count1 = {}
        for i in xrange(len(list1)):
            count1[list1[i]] = i
        smallest = None
        for i in xrange(len(list2)):
            s2 = list2[i]
            if s2 in count1:
                smallest = i + count1[s2] if smallest == None else  min(smallest, i + count1[s2])
        result = []
        for i in xrange(len(list2)):
            s2 = list2[i]
            if s2 in count1 and i + count1[s2] == smallest:
                result.append(s2)
        return result