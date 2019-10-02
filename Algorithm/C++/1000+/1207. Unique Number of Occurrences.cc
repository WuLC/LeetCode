#include <unordered_map>
#include <unordered_set>
#include <vector>

class Solution {
public:
    bool uniqueOccurrences(std::vector<int>& arr) {
        std::unordered_map<int, int> count;
        for (auto num: arr) {
          count[num]++;
        }
        std::unordered_set<int> unique;
        for (auto e : count) {
          unique.insert(e.second);
        }
        return count.size() == unique.size();
    }
};