# naive solution, O(mn)
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [i for i in range(n+1)]
        for i in range(n):
            for word in dictionary:
                idx = i - len(word) + 1 
                if idx >= 0 and s[idx : i+1] == word:
                    dp[i+1] = min(dp[i+1], dp[i-len(word)+1])
                dp[i+1] = min(dp[i]+1, dp[i+1])
        return dp[-1]
