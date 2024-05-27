#include <string>
#include <unordered_set>

class Solution {
public:
    int maxUniqueSplit(std::string s) {
       std::unordered_set<std::string> candidate;
       return dfs(s, candidate, 0);
    }

private:
    int dfs(std::string& s, std::unordered_set<std::string>& candidate, int idx) {
        if (idx == s.length()) {
            return candidate.size();
        }
        int result = 1;
        for (int i = idx; i < s.length(); i++) {
            std::string substr = s.substr(idx, i-idx+1);
            if (candidate.find(substr) == candidate.end()) {
                candidate.insert(substr);
                result = std::max(dfs(s, candidate, i+1), result);
                candidate.erase(substr);
            }
        }
        return result;
    }
};