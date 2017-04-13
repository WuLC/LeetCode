# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2017-04-13 19:08:44
# @Last modified by:   WuLC
# @Last Modified time: 2017-04-13 19:09:44
# @Email: liangchaowu5@gmail.com


# use hashmap and count the positions the don't cross the brick
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        count = {}
        for i in xrange(len(wall)):
            position = 0
            for j in xrange(len(wall[i])-1):
                position += wall[i][j]
                count.setdefault(position, 0)
                count[position] += 1
        return len(wall) - max(count.values()) if len(count) > 0 else len(wall)