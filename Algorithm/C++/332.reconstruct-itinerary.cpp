/*
 * @lc app=leetcode id=332 lang=cpp
 *
 * [332] Reconstruct Itinerary
 */

// @lc code=start
#include <unordered_map>
#include <map>
#include <vector>
#include <string>

class Solution {
public:
    std::vector<std::string> findItinerary(std::vector<std::vector<std::string>>& tickets) {
        paths.clear();
        result.clear();
        for (auto t : tickets) {
            paths[t[0]][t[1]]++;
        }
        result.push_back("JFK");
        dfs("JFK", tickets);
        return result;
    }

private:
    std::unordered_map<std::string, std::map<std::string, int>> paths;
    std::vector<std::string> result;

    bool dfs(std::string start, std::vector<std::vector<std::string>>& tickets) {
        if (result.size() == tickets.size() + 1) {
            return true;
        }

        for (auto iter = paths[start].begin(); iter != paths[start].end(); iter++) {
            if (iter->second > 0) {
                paths[start][iter->first]--;
                result.push_back(iter->first);
                if (dfs(iter->first, tickets)) {
                    return true;
                }
                result.pop_back();
                paths[start][iter->first]++;
            }
        }
        return false;
    }
};
// @lc code=end

