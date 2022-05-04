/*
 * @lc app=leetcode id=69 lang=cpp
 *
 * [69] Sqrt(x)
 */

// @lc code=start
#include <cmath>

class Solution {
public:
    int mySqrt(int x) {
        int mid, left = 0, right = x;
        long long num;
        while (left <= right) {
           mid = left + ((right-left)>>1);
           num = std::pow(mid, 2);
           if (num == x) {
               return mid;
           } else if (num > x) {
               right = mid - 1;
           } else {
               left = mid + 1;
           }
        }
        if (std::pow(left, 2) < num) {
           return left;
        } else {
           return left - 1;
        }
    }
};
// @lc code=end

