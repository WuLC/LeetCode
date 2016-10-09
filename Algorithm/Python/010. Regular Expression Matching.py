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
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        dp = [ [False for i in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True # dp[i][j]表示s[:i-1] 和 p[:j-1]是否符合正则表达
        
        # 处理s[1]在比较中用到的dp[0]的初始化问题，没有这段代码就出错例子(aab,c*a*b)
        # 可以理解为当 S 为空时,所有的*都必须表示为前面字符的0个字符
        for i in range(1,len(p)+1):
            if p[i-1]=='*' and i>=2:
                    dp[0][i]=dp[0][i-2]  

        #DP 处理的核心代码
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1] 
                elif p[j-1] =='*':
                    dp[i][j] = dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (p[j-2] == s[i-1] or p[j-2] == '.'))
                else:
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1])
        return dp[len(s)][len(p)]
   


'''
递归超时测试例子
if __name__ == '__main__':
    s = Solution()
    print s.isMatch('aaaaaaaaaaaaab','a*a*a*a*a*a*a*a*a*a*c')

'''