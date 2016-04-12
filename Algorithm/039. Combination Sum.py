# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-04-11 15:48:31
# @Last modified by:   WuLC
# @Last Modified time: 2016-04-12 10:16:19
# @Email: liangchaowu5@gmail.com


# solution-1,backtracking
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

# solution-2,DP
class Solution(object):
    def combinationSum(self, candidates, target):
        dp = {}
        dp[0] = []
        for i in xrange(1,target+1):
            dp [i] = []
            if i in candidates:
                dp[i].append([i])
            for j in xrange(1,i/2+1):
                if len(dp[j]) ==0 or len(dp[i-j])==0:
                    continue
                for m in dp[j]:
                    for k in dp[i-j]:
                        tmp = m+k
                        tmp.sort()
                        if tmp not in dp[i]:
                            dp[i].append(tmp)
        return dp[target]
