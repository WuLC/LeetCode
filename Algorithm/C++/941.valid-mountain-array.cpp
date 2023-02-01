/*
 * @lc app=leetcode id=941 lang=cpp
 *
 * [941] Valid Mountain Array
 */

// @lc code=start
#include <vector>

class Solution {
public:
    bool validMountainArray(std::vector<int>& arr) {
        int idx = 0;
        for (int i = 1; i < arr.size(); i++) {
            if (arr[i] > arr[idx]) {
                idx = i;
            }
        }
        bool left = false, right = false;
        int i = idx, j = idx;
        while (i > 0) {
            if (arr[i] > arr[i-1]) {
                left = true;
            } else {
                return false;
            }
            i--;
        }
        while (j < arr.size()-1) {
            if (arr[j] > arr[j+1]) {
                right = true;
            } else {
                return false;
            }
            j++;
        }
        return left && right;
    }
};
// @lc code=end

