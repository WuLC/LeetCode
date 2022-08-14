/*
 * @lc app=leetcode id=135 lang=cpp
 *
 * [135] Candy
 */

// @lc code=start
#include <vector>
#include <numeric>

class Solution {
public:
    int candy(std::vector<int>& ratings) {
        std::vector<int> candies(ratings.size(), 1);

        // make left->right legal
        for (int i = 0; i < ratings.size() - 1; i++) {
            if (ratings[i+1] > ratings[i]) {
                candies[i+1] = candies[i] + 1;
            }
        }

        // make right->left legal
        for (int i = ratings.size() - 1; i > 0; i--) {
            if (ratings[i-1] > ratings[i]) {
                candies[i-1] = std::max(candies[i-1], candies[i]+1);
            }
        }

        return std::accumulate(candies.begin(), candies.end(), 0);
    }
};
// @lc code=end

