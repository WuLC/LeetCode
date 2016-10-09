# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-04-12 10:52:14
# @Last modified by:   WuLC
# @Last Modified time: 2016-04-13 09:29:04
# @Email: liangchaowu5@gmail.com

# DP
# candidates中的元素只能用一次，但是candidates中可能有重复的元素
class Solution(object):
    def combinationSum2(self, candidates, target):
    	can_dict = {}
    	for candidate in candidates:
    		if candidate not in can_dict: 
    		    can_dict[candidate] = 0
    		can_dict[candidate] += 1

        dp = {}
        dp[0] = []
        for i in xrange(1,target+1):
            dp[i] = []
            if i in candidates:
                dp[i].append([i])
            for j in xrange(1,i/2+1):
                if len(dp[j])==0 or len(dp[i-j])==0:
                    continue
                for m in dp[j]:
                    for n in dp[i-j]:
                        tmp_dict = {}
                        flag = 0               
                        tmp = m+n
                        for t in tmp:
                            if t not in tmp_dict: 
                                tmp_dict[t] = 0
                            tmp_dict[t] += 1
                       
                        for te in tmp_dict:
                            if tmp_dict[te] > can_dict[te]: 
	                            flag = 1
	                            break
                        if flag == 0:
                            tmp.sort()                         
                            if tmp not in dp[i]:
                                dp[i].append(tmp)
        return dp[target]

# bracktracking
class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        self.dfs(candidates,target,0 ,[],result)
        return result


    def dfs(self, nums, tar, index, tmp, res):
        if tar == 0 :
            if tmp not in res:
                res.append(tmp)
        else:
            for i in range(index,len(nums)):
                if tar-nums[i]<0:
                    return
                self.dfs(nums, tar-nums[i], i+1, tmp+[nums[i]], res)
