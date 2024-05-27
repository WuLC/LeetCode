class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        def dfs(candidate, idx, result):
            if idx == len(s):
                result[0] = max(result[0], len(candidate))
                return
            for i in range(idx, len(s)):
                sub = s[idx: i+1]
                if sub not in candidate:
                    candidate.add(sub)
                    dfs(candidate, i+1, result)
                    candidate.remove(sub)
        
        result, candidate = [1], set()
        dfs(candidate, 0, result)
        return result[0]
        
        # # yet another more concise solution
        # result, candidate = [1], set()
        # def dfs(idx):
        #     if idx == len(s):
        #         result[0] = max(result[0], len(candidate))
        #         return
        #     for i in range(idx, len(s)):
        #         sub = s[idx: i+1]
        #         if sub not in candidate:
        #             candidate.add(sub)
        #             dfs(i+1)
        #             candidate.remove(sub)
        # dfs(0)
        # return result[0]