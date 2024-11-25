class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        n = len(nums)
        cnt = [0]*(n+1)
        for s, e in queries:
            cnt[s]+=1
            cnt[e+1]-=1

        curr_cnt = 0
        for i in range(n):
            curr_cnt += cnt[i]
            if curr_cnt < nums[i]:
                return False
        return True
            