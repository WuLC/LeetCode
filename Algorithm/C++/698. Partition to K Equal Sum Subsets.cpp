/*
 * Created on Fri May 04 2018 14:52:56
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// dfs, AC
class Solution 
{
    public:
        bool canPartitionKSubsets(vector<int>& nums, int k) 
        {
            int sum = std::accumulate(nums.begin(), nums.end(), 0);
            if (sum%k != 0) return false;
            std::sort(nums.begin(), nums.end());
            return dfs(nums, k, sum/k, 0, 0);
        }
        
        bool dfs(vector<int>& nums, int k, int target, int idx, int tmp)
        {
            if (k==0) return true;
            if (target == tmp) return dfs(nums, k-1, target, 0, 0);
            for(int i=idx; i<nums.size(); i++)
            {
                if (nums[i] == -1) continue;
                if (nums[i]+tmp > target) return false;
                int pre = nums[i];
                nums[i] = -1;
                if (dfs(nums, k, target, i+1, tmp+pre)) return true;
                nums[i] = pre;
            }
            return false;
        }
};