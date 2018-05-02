/*
 * Created on Wed May 02 2018 17:3:22
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// dfs, TLE for some cases
class Solution 
{
    public:
        bool canPartition(vector<int>& nums) 
        {
            int sum = std::accumulate(nums.begin(), nums.end(), 0);
            std::sort(nums.begin(), nums.end());
            if(sum%2 != 0 || nums.back() > sum/2) return false;
            return dfs(nums, sum>>1, 0, 0);
        }

        bool dfs(vector<int>& nums, int target, int tmp, int idx)
        {
            if(tmp == target) return true;
            for(int i = idx; i < nums.size(); i++)
            {
                if (tmp+nums[i] > target) break;
                if (dfs(nums, target, tmp+nums[i], i+1)) return true;
            }
            return false;
        }
};

// dp, AC
class Solution 
{
    public:
        bool canPartition(vector<int>& nums) 
        {
            int sum = std::accumulate(nums.begin(), nums.end(), 0);
            if(sum%2 != 0) return false;
            int target = sum>>1;
            bool dp[target+1] = {false};
            dp[0] = true;
            for(int num:nums)
            {
                for(int i=target; i>=num; i--) // traverse from end to start to avoid the case like [1, 2, 5] where 2 may be used repeatedly
                {
                    if (dp[i-num]) dp[i] = true;
                    if (dp[target]) return true;
                }
            }
            return false;
        }
};