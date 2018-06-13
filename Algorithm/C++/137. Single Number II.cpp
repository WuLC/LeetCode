/*
 * Created on Wed Jun 13 2018 19:27:42
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// bit manipulation, expand the problem to k same number
class Solution 
{
    public:
        int singleNumber(vector<int>& nums) 
        {
            return uniqueOfK(nums, 3);
        }
    
        int uniqueOfK(vector<int> nums, int k)
        {
            int result = 0;
            for(int i=0; i<32; i++)
            {
                int count=0;
                for(int num:nums)
                    if ((num&(1<<i)) != 0) count++;
                if (count%k != 0)
                    result ^= (1<<i);
            }
            return result;
        }
};
