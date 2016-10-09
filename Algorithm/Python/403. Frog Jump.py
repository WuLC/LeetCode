# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-10-06 11:39:22
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-06 20:14:10
# @Email: liangchaowu5@gmail.com

# DP
# time complexity O(n^2), TLE
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        jumps = [set() for _ in xrange(len(stones))]
        jumps[0].add(0)
        for i in xrange(len(stones)):
            # deal with the first step
            if i == 1:
                if stones[i] - stones[0] == 1:
                    jumps[i].add(1)
                continue
            for j in xrange(i):
                if len(jumps[j]) > 0:
                    tmp = stones[i]-stones[j]
                    if any([num in jumps[j] for num in [tmp-1, tmp, tmp+1]]):
                        jumps[i].add(tmp)
        return len(jumps[-1])>0
            
            

# greedy
# time complexity, O(n)
# at each index, reach all the places that it can jump
# use hash map to store the  value of each stone and all the possible last steps that taken to reach the stone
# two versions, the first version is short but cost more space without checking 
# the second checks whether the target is in the stones and stop once reaching the destination
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        jumps = collections.defaultdict(set)
        jumps[stones[0]].add(0)
        for i in xrange(len(stones)):
            if stones[i] in jumps:
                for num in jumps[stones[i]]:
                    if num - 1 > 0:
                        jumps[stones[i] + num- 1].add(num -1)
                    jumps[stones[i] + num].add(num)
                    jumps[stones[i] + num + 1].add(num + 1)
        return stones[-1] in jumps
            
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        nums = set(stones)
        jumps = collections.defaultdict(set)
        jumps[stones[0]].add(0)
        for i in xrange(len(stones)):
            if stones[i] in jumps:
                for num in jumps[stones[i]]:
                    tmp = stones[i] + num
                    if num - 1 > 0 and tmp - 1 in nums:
                        jumps[tmp - 1].add(num -1)
                        if tmp - 1 == stones[-1]:
                            return True
                    if tmp in nums:
                        jumps[tmp].add(num)
                        if tmp == stones[-1]:
                            return True
                    if tmp + 1 in nums:
                        jumps[tmp + 1].add(num + 1)
                        if tmp + 1 == stones[-1]:
                            return True
        return False            
            