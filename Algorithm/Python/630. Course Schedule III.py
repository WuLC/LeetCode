# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-06-25 15:44:40
# @Last Modified by:   WuLC
# @Last Modified time: 2017-06-25 15:56:35

import heapq

class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses.sort(key = lambda x:x[1])
        course_time = []
        curr_date = 0
        for c in courses:
            curr_date += c[0]
            heapq.heappush(course_time, -c[0])
            while curr_date > c[1]:
                curr_date -= heapq.heappop(course_time)
        return len(course_time)