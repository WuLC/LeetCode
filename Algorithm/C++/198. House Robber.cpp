/*
 * Created on Fri Apr 20 2018 1:35:40
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// dp with O(1) space
class Solution 
{
    public:
        int rob(vector<int>& nums) 
        {
            int pre=0, curr=0, result=0, tmp;
            for(int i=0; i<nums.size(); i++)
            {
                tmp = curr;
                curr = max(pre+nums[i], curr);
                pre = tmp;
                result = max(result, curr);
            }
            return result;
        }
};