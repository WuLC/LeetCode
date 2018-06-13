/*
 * Created on Wed Jun 13 2018 13:15:25
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// bit manipulation, use the last bit to differ the two numbers
class Solution 
{
    public:
        vector<int> singleNumber(vector<int>& nums) 
        {
            int n = 0;
            for(auto num : nums)
                n ^= num;
            int diff = n&(-n);
            int num1 = 0, num2 = 0;
            for(auto num : nums)
            {
                if((num&diff) != 0) num1 ^= num;
                else num2 ^= num;
            }
            vector<int> result = {num1, num2};
            return result;
        }
};