#include <vector>

class Solution {
    public:
        int returnToBoundaryCount(std::vector<int>& nums) {
            int result = 0, curr = 0;
            for (auto num: nums) {
                curr += num;
                if (curr == 0) result++;
            }
            return result;
        }
    };