/*
 * Created on Sun Apr 22 2018 15:59:15
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// since 0 and n-1 cannot be robbed at the same time 
// divide the problem into 2 cases: (0,n-2) and (1, n-1), the get the max result of them 
class Solution 
{
    public:
        int rob(vector<int>& nums) 
        {
            int n = nums.size();
            if (n <= 1) return n==0 ? 0 : nums[0];
            return max(helper(nums, 0, n-2), helper(nums, 1, n-1));
        }
        
        int helper(vector<int>& nums, int left, int right)
        {
            int pre = 0, curr = 0;
            for(int i=left; i<=right; i++)
            {
                int tmp = curr;
                curr = max(pre+nums[i], curr);
                pre = tmp;
            }
            return curr;
        }
};