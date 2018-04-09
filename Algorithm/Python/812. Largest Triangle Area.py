# -*- coding: utf-8 -*-
# Created on Mon Apr 09 2018 15:45:58
# Author: WuLC
# EMail: liangchaowu5@gmail.com

# get the area of triangle with Heron's formula
# reference https://en.wikipedia.org/wiki/Heron%27s_formula
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        n = len(points)
        result = 0
        for i in xrange(n):
            for j in xrange(i+1, n):
                for k in xrange(j+1, n):
                    result = max(result, self.area(points[i], points[j], points[k]))
        return result
            
        
    def area(self, p1, p2, p3):
        a = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5
        b = ((p1[0] - p3[0])**2 + (p1[1] - p3[1])**2) ** 0.5
        c = ((p2[0] - p3[0])**2 + (p2[1] - p3[1])**2) ** 0.5
        if a+b <= c or a+c <=b or b+c <= a: # three points may not be able to contruct a triangle
            return 0
        s = (a+b+c)/2.0
        return (s*(s-a)*(s-b)*(s-c))**0.5