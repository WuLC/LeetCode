#include <vector>

class Solution {
public:
    int minZeroArray(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        int n = nums.size();
        int idx = 0, curr_sum = 0;
        std::vector<int> counter(n+1, 0);
        for(int i = 0; i < n; i++) {
            curr_sum += counter[i];
            while(curr_sum < nums[i] && idx < queries.size()) {
                int l = queries[idx][0], r = queries[idx][1], v = queries[idx][2];
                counter[l] += v;
                counter[r+1] -= v;
                if (l <= i && i <= r) {
                    curr_sum += v;
                }
                idx++;
            }
            if (idx == queries.size() && curr_sum < nums[i]) {
                return -1;
            }
        }
        return idx;
    }
};