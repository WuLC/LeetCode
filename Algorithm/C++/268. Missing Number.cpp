/*
 * Created on Wed Jun 13 2018 20:1:34
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// swap numbers in place
class Solution 
{
    public:
        int missingNumber(vector<int>& nums) 
        {
            int n = nums.size(), tmp;
            for(int i=0; i<n; i++)
            {
                while(nums[i] != n && nums[nums[i]] != nums[i])
                {
                    tmp = nums[nums[i]];
                    nums[nums[i]] = nums[i];
                    nums[i] = tmp;
                }
            }
            for(int i=0; i<n; i++)
                if (nums[i] != i)
                    return i;
            return n;
        }
};