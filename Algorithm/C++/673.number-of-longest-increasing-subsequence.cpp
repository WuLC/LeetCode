/*
 * @lc app=leetcode id=673 lang=cpp
 *
 * [673] Number of Longest Increasing Subsequence
 */

// @lc code=start

#include <vector>

class Solution {
public:
    int findNumberOfLIS(std::vector<int>& nums) {
        int n = nums.size();
        int max_len = 1;
        std::vector<int> length(n, 1), count(n, 1);
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j] && length[i] <= length[j]+1) {
                    if (length[i] == length[j]+1) {
                        count[i] += count[j];
                    } else {
                        count[i] = count[j];
                    }
                    length[i] = length[j]+1;
                }
            }
            max_len = std::max(max_len, length[i]);
        }
        int result = 0;
        for (int i = 0; i < n; i++) {
            if (length[i] == max_len) {
                result += count[i];
            }
        }
        return result;
    }
};
// @lc code=end

