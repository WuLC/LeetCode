# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-04-11 15:48:31
# @Last modified by:   LC
# @Last Modified time: 2016-04-11 15:49:03
# @Email: liangchaowu5@gmail.com


class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target == 0:
            res.append(path)
            return 
        for i in xrange(index, len(nums)):
            if target-nums[i] < 0:
                return  # backtracking
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)