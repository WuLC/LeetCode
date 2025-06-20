#include <vector>

class Solution {
    public:
        std::vector<std::vector<int>> divideArray(std::vector<int>& nums, int k) {
            std::vector<std::vector<int>> result;
            int n = nums.size();
            std::sort(nums.begin(), nums.end());
            for (int i = 0; i < n - 2; i += 3) {
                if (nums[i+2] - nums[i] > k) {
                    return std::vector<std::vector<int>>();
                } else {
                    result.push_back(std::vector<int>{nums[i], nums[i+1], nums[i+2]});
                }
            }
            return result;
        }
    };