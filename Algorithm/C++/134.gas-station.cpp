/*
 * @lc app=leetcode id=134 lang=cpp
 *
 * [134] Gas Station
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int canCompleteCircuit(std::vector<int>& gas, std::vector<int>& cost) {
        int n = gas.size(), idx = 0, count = 0, curr_sum = 0;
        int result = -1;
        while (idx < n) {
            int ni, new_idx = idx;
            for (int i = 0; i < n; i++) {
                ni = (idx + i) % n;
                curr_sum += gas[ni] - cost[ni];
                if (curr_sum < 0) {
                    count = 0;
                    curr_sum = 0;
                    new_idx = ni + 1;
                    break;
                }
                count++;
            }
            if (count == n) {
                result = idx;
                break;
            }
            idx = std::max(idx + 1, new_idx);
        }
        return result;
    }
};
// @lc code=end

