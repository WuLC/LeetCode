
# Solution1，AC, avg time complexity max(O(m*n), max(O(m^3), O(n^3))
# (1) find longest common substring of two strings 
#（2) find longest substr of each string, cancate it after the result of first step

class Solution(object):
    def longestPalindrome(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        t = t[::-1]
        m, n = len(s), len(t)
        s_pal, t_pal = self.longestPalindromeStarted(s), self.longestPalindromeStarted(t)
        dp = [[0] * (n+1) for _ in range(m+1)]
        result = 1
        for i in range(m):
            for j in range(n):
                if s[i] == t[j]:
                    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
                tmp = dp[i+1][j+1]*2
                # get longest palindrome substr from index i or i+1
                if tmp == 0:
                    tmp += max(s_pal[i], t_pal[j])
                else:
                    if i+1 < m and j+1 <n:
                        tmp += max(s_pal[i+1], t_pal[j+1])
                    elif i+1 < m:
                        tmp += s_pal[i+1]
                    elif j+1 < n:
                        tmp += t_pal[j+1]
                result = max(result, tmp)
        return result   
    
    def longestPalindromeStarted(self, s):
        n = len(s)
        result = [1] * n
        for i in range(n):
            for j in range(n-1, i, -1):
                l, r = i, j
                while l < r:
                    if s[l] != s[r]:
                        break
                    l += 1
                    r -= 1
                if l >= r:
                    result[i] = j - i + 1
                    break
        
        return result


# Solution2, WA
# (1)find longest common substring of two strings 
# (2)longest palidrome substring of single string
# but can not deal with case like "hc" and "jooh"
class Solution(object):
    def longestPalindrome(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        t = t[::-1]
        # longest common substring of two strings
        m, n = len(s), len(t)
        dp = [[0] * (n+1) for _ in range(m+1)]
        result = 1
        for i in range(m):
            for j in range(n):
                if s[i] == t[j]:
                    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
                    if dp[i+1][j+1]*2 >= result:
                        result = dp[i+1][j+1]*2
                        if i != m-1 or j != n-1:
                            result += 1
        return max(result, max(self.longestPalindromeSubstr(s), self.longestPalindromeSubstr(t)))    
    
    def longestPalindromeSubstr(self, s):
        n = len(s)
        def expand_from_center(left, right):
            l, r = left, right
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        
        result = 1
        for i in range(n):
            result = max(result, expand_from_center(i, i))
            result = max(result, expand_from_center(i, i+1))
        return result


            