/*
 * @lc app=leetcode id=347 lang=cpp
 *
 * [347] Top K Frequent Elements
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <queue>
#include <utility>

// hashmap + heap, avg time complexity O(n*lgk)
class Solution {
public:
    std::vector<int> topKFrequent(std::vector<int>& nums, int k) {
        std::unordered_map<int, int> counter;
        for (auto num: nums) counter[num]++;

        // build heap
        auto cmp = [](std::pair<int, int> p1, std::pair<int, int> p2) {
            return p1.second > p2.second;
        };    
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, decltype(cmp)> que(cmp);

        for (auto itr : counter) {
            // que.push(std::make_pair(itr.first, itr.second));
            que.push(std::move(itr));
            if (que.size() == k+1) {
                que.pop();
            }
        }
        
        std::vector<int> result;
        while(!que.empty()) {
            result.push_back(que.top().first);
            que.pop();
        }
        return result;
    }
};
// @lc code=end

