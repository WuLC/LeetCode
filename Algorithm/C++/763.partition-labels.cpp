/*
 * @lc app=leetcode id=763 lang=cpp
 *
 * [763] Partition Labels
 */

// @lc code=start
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>

class Solution {
public:
    std::vector<int> partitionLabels(std::string s) {
        std::unordered_map<char, std::vector<int>> char_range;
        for (int i = 0; i < s.size(); i++) {
            if (char_range.find(s[i]) == char_range.end()) {
                char_range[s[i]] = std::vector<int>{i, i};
            } else {
                char_range[s[i]][1] = i;
            }
        }

        std::vector<std::vector<int>> intervals; // intervals(char_range.size()) will cause error
        intervals.reserve(char_range.size()); // user reserve() instead
        for (auto& iter: char_range) {
            intervals.emplace_back(iter.second);
        }
        std::sort(intervals.begin(), intervals.end(), [](const std::vector<int>& v1, const std::vector<int>& v2)->bool {
            if (v1[0] != v2[0]) {
                return v1[0] < v2[0];
            } else {
                return v1[1] < v2[1];
            }
        });
        
        std::vector<int> result;
        int pre_start = intervals[0][0], pre_end = intervals[0][1];
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] < pre_end) {
                pre_end = std::max(pre_end, intervals[i][1]);
            } else {
                result.push_back(pre_end - pre_start + 1);
                pre_start = intervals[i][0];
                pre_end = intervals[i][1];
            }
        }
        result.push_back(pre_end - pre_start + 1);
        return result;
    }
};
// @lc code=end

