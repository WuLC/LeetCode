# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-09-04 20:41:18
# @Last Modified by:   WuLC
# @Last Modified time: 2017-09-04 20:47:02


# there are only 4 kinds of operations, each operation may be carried or not(0 or 1), so there are at most 16 situations
# from (0, 0, 0, 0) to (1, 1, 1, 1)
# moreover as 1 + 2 ->3, 1 + 3 -> 2, 2 + 3 ->1
# so all possible situations are: All_on, 1, 2, 3, 4, 1+4, 2+4, 3+4
# that's to say, there're at most 8 kinds of situations, and the first 3 lights can represent them

class Solution(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 1
        if n == 1:
            return 2
        if n == 2:
            return 3 if m == 1 else 4
        if n >= 3:
            if m == 1:
                return 4
            elif m == 2:
                return 7
            else:
                return 8