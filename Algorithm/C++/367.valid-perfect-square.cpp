/*
 * @lc app=leetcode id=367 lang=cpp
 *
 * [367] Valid Perfect Square
 */

// @lc code=start

#include <cmath>

class Solution {
public:
    bool isPerfectSquare(int num) {
        int mid, left = 0, right = num;
        long long val;
        while (left <= right) {
           mid = left + ((right-left)>>1);
           val = std::pow(mid, 2);
           if (val == num) {
               return true;
           } else if (val > num) {
               right = mid - 1;
           } else {
               left = mid + 1;
           }
        }
        return false;
    }
};
// @lc code=end

