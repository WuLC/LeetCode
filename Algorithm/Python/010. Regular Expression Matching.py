# -*- coding: utf-8 -*-
# @Author: LC
# @Date:   2016-02-28 19:53:51
# @Last modified by:   LC
# @Last Modified time: 2016-04-10 16:24:12
# @Email: liangchaowu5@gmail.com

# 实现. 和 * 正则表达的功能，
# 参考：http://www.cnblogs.com/zuoyuan/p/3781773.html

#递归实现,超时
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        if len(p)==0:
            return len(s)==0
        if len(p)==1:
            if len(s)!=1 or ( s[0]!=p[0] and p[0]!='.' ):
                return False
            else: # len(s)==1 and (s[0]==p[0] or p[0] =='.')
                return True
        #len(p)>=2
        if p[1]!='*':
            if len(s) <= 1 or (p[0]!='.' and p[0]!=s[0]):
                return False
            else:
                return self.isMatch(s[1:],p[1:])
        else: #p[1]='*'
            i=0
            lenS=len(s)
            if p[0]=='.' :
                while i<lenS:
                    if self.isMatch(s[i:],p[2:]):
                        return True
                    i+=1
            else:
                while i<lenS and p[0] == s[i]:
                    if self.isMatch(s[i:],p[2:]):
                        return True
                    i+=1
            return False

# DP实现
class Solution(object):
    def isMatch(self, s, pattern):
        m, n = len(pattern), len(s)
        dp = [[False for j in xrange(n+1)] for i in xrange(m+1)]
        dp[0][0] = True
        for i in xrange(1, m+1):
            for j in xrange(n+1):
                if j==0:
                    if pattern[i-1] == '*' and i-2 >= 0:
                        dp[i][j] = dp[i-2][j]
                elif pattern[i-1] == s[j-1] or pattern[i-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif pattern[i-1] == '*':
                    dp[i][j] = dp[i-2][j] or dp[i-1][j] or ((pattern[i-2] == s[j-1] or pattern[i-2] == '.') and dp[i][j-1])
        return dp[m][n]