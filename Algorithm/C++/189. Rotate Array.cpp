/*
 * Created on Fri May 18 2018 19:3:44
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// simple solution
class Solution
{
    public:
        void rotate(vector<int>& nums, int k)
        {
            for(int i=0; i<k; i++)
            {
                nums.insert(nums.begin(), nums.back());
                nums.pop_back();
            }
        }
};