/*
 * @lc app=leetcode id=1814 lang=cpp
 *
 * [1814] Count Nice Pairs in an Array
 */

// @lc code=start
#include <vector>
#include <string>
#include <unordered_map>

class Solution {
public:
    int countNicePairs(std::vector<int>& nums) {
        std::unordered_map<int, int> counter;
        for (auto num: nums) {
            int diff = num - rev(num);
            if (counter.find(diff) != counter.end()) {
                counter[diff]++;
            } else {
                counter[diff] = 1;
            }
        }
        long long result = 0;
        for (auto p: counter) {
            result += (long(p.second-1)*p.second/2)%1000000007;
            result %= 1000000007;
        }
        return result;
    }

private:
    int rev(int num) {
        std::string str = std::to_string(num);
        int result = 0;
        for (int i = str.size()-1; i >= 0; i--) {
            result = result * 10 + (str[i] - '0');
        }
        return result;
    }

};
// @lc code=end

