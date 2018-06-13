/*
 * Created on Wed Jun 13 2018 12:6:59
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// xor
class Solution 
{
public:
    int singleNumber(vector<int>& nums) 
    {
        int result = 0;
        for(auto num:nums)
            result ^= num;
        return result;
    }
};