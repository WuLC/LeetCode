#include <vector>
class Solution {
    public:
        int maximumDifference(std::vector<int>& nums) {
            int n = nums.size();
            std::vector<int> prefix_min;
            prefix_min.reserve(n);

            int curr_min = nums[0];
            for (int i = 0; i < n; i++) {
                curr_min = std::min(curr_min, nums[i]);
                prefix_min.push_back(curr_min);
            }

            int result = -1, curr_max = nums[n-1];
            for (int i = n-1; i > 0; i--) {
                curr_max = std::max(curr_max, nums[i]);
                if (curr_max - prefix_min[i-1] > 0) {
                    result = std::max(result, curr_max - prefix_min[i-1]);
                }
            }
            return result;
        }
    };