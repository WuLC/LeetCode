# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-05-21 15:20:45
# @Last modified by:   WuLC
# @Last Modified time: 2017-05-21 15:23:10
# @Email: liangchaowu5@gmail.com


# judge if there are only two kinds of length between points firstly
# then find the neighbors of p1 with the shortest length and judge if the neighboring edge are orthogonal
from math import sqrt
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        def distance(a, b):
            return (a[0]-b[0])**2+(a[1]-b[1])**2
            
        record = set()
        points = [p1, p2, p3, p4]
        for i in xrange(4):
            for j in xrange(i+1, 4):
                record.add(distance(points[i], points[j]))
        if len(record) != 2:
            return False
            
        edge = min(record)
        p1_neighbors = []
        for p in points:
            if distance(p, p1) == edge:
                p1_neighbors.append(p)
        p1_vectors = map(lambda p: (p[0]-p1[0], p[1]-p1[1]), p1_neighbors)
        if len(p1_vectors) != 2: # case [0,0], [1,1], [0,0], [0,0]
            return False
        else:
            return True if reduce(lambda p,q : p[0]*q[0]+p[1]*q[1], p1_vectors) == 0 else False
        