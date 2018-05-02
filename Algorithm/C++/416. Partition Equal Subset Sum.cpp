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

