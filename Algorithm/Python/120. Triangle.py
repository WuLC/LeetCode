# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-07-12 12:19:31
# @Last modified by:   WuLC
# @Last Modified time: 2016-07-12 12:27:17
# @Email: liangchaowu5@gmail.com

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        min_path, extra_point = [], None
        for i in xrange(len(triangle)):
            tmp = min_path[:]
            for j in xrange(len(triangle[i])):
                if i==0:
                    min_path.append(triangle[i][j])
                    break
                if j==0:
                    min_path[j] += triangle[i][j]
                elif j == len(triangle[i])-1:
                    min_path.append(tmp[-1]+triangle[i][j])
                else:
                    min_path[j] = min(tmp[j]+triangle[i][j], tmp[j-1]+triangle[i][j])
        return min(min_path)