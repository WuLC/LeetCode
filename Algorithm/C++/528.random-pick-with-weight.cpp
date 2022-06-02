/*
 * @lc app=leetcode id=528 lang=cpp
 *
 * [528] Random Pick with Weight
 */

// @lc code=start

#include <vector>
#include <random>

class Solution {
public:
    Solution(std::vector<int>& weights) {
        int sum = 0;
        for (auto num: weights) {
            sum += num;
        }
        float curr_sum = 0, prob;
        for (auto num: weights) {
            prob = num*1.0/sum;
            range.push_back(std::vector<float>{curr_sum, curr_sum + prob});
            curr_sum += prob;
        }
    }
    
    int pickIndex() {
        double target = std::rand()/double(RAND_MAX);
        int left = 0, right = range.size() - 1, mid;
        while (left < right) {
            mid = left + ((right - left)>>1);
            if (range[mid][0] <= target && target < range[mid][1]) {
                return mid;
            } else if (range[mid][0] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

private:
    std::vector<std::vector<float>> range;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */
// @lc code=end

