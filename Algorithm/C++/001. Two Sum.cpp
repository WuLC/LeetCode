/*
 * Created on Thu Apr 12 2018 19:17:19
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// O(n) time, O(n) space
class Solution 
{
    public:
        vector<int> twoSum(vector<int>& nums, int target) 
        {
            unordered_map<int, int> hashMap;
            vector<int> result;
            for(int i=0; i<nums.size(); i++)
            {
                int leftNumber = target - nums[i];
                if(hashMap.find(leftNumber) != hashMap.end())
                {
                    result.push_back(hashMap[leftNumber]);
                    result.push_back(i);
                    return result;
                }
                hashMap[nums[i]] = i;
            }
        }
};