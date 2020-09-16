#include <string>
#include <vector>

// greedy, O(m+n) time

class Solution {
public:
    bool isTransformable(std::string s, std::string t) {
        std::vector<std::vector<int>> idx(10);
        std::vector<int> counter(10, 0);
        for(int i=0; i<s.size(); i++)
            idx[s[i]-'0'].push_back(i);
        for(char c : t) {
            int val = c - '0';
            if (counter[val] >= idx[val].size()) return false;
            for (int i=0; i<val; i++)
                if (counter[i] < idx[i].size() && idx[i][counter[i]] < idx[val][counter[val]])
                    return false;
            counter[val]++;
        }
        return true;
    }
};