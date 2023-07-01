/*
 * @lc app=leetcode id=1471 lang=cpp
 *
 * [1471] The k Strongest Values in an Array
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> getStrongest(std::vector<int>& arr, int k) {
        std::sort(arr.begin(), arr.end());
        int mid = arr[int((arr.size()-1)/2)];

        int left = 0, right = arr.size() - 1;
        std::vector<int> result;
        result.reserve(k);
        while (k > 0) {
            if (std::abs(arr[right] - mid) >= std::abs(arr[left] - mid)) {
                result.push_back(arr[right]);
                right--;
            } else {
                result.push_back(arr[left]);
                left++;
            }
            k--;
        }
        return result;
    }
};
// @lc code=end

