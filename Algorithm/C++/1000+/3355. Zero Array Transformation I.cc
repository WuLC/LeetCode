#include <vector>

class Solution {
    public:
        bool isZeroArray(std::vector<int>& nums, std::vector<vector<int>>& queries) {
            int n = nums.size();
            std::vector counter(n+1, 0);
            for (auto q : queries) {
                counter[q[0]]++;
                counter[q[1]+1]--;
            }
            int curr_cnt = 0;
            for (int i = 0; i < n; i++) {
                curr_cnt += counter[i];
                if (curr_cnt < nums[i]) {
                    return false;
                }
            }
            return true;
        }
};