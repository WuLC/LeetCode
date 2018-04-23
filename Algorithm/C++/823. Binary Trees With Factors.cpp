/*
 * Created on Mon Apr 23 2018 16:42:22
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// dp
class Solution 
{
    public:
        int numFactoredBinaryTrees(vector<int>& A) 
        {
            long result = 0, mod = pow(10, 9)+7;
            unordered_map<int, long> dp;
            sort(A.begin(), A.end());
            for(int i=0; i<A.size(); i++)
            {
                dp[A[i]] = 1;
                for(int j = 0; j <= i; j++) 
                {
                    if (A[i]%A[j] == 0 && dp.find(A[i]/A[j]) != dp.end())
                        dp[A[i]] += dp[A[j]]*dp[A[i]/A[j]];
                }
                dp[A[i]] %= mod;
                result += dp[A[i]];
                result %= mod;
            }
            return result;
        }
};