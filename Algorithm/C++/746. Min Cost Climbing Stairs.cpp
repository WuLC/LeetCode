/*
 * Created on Wed May 02 2018 10:39:32
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// dp, O(n) space
// pay attention that top means exceed the last element of the array
class Solution 
{
    public:
        int minCostClimbingStairs(vector<int>& cost)
        {
            std::vector<int> dp = {0,0};
            for(int i=2; i<=cost.size(); i++)
                dp.push_back(std::min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2]));
            return dp.back();
        }
};