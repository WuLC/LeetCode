#include <string>
#include <vector>

class Solution {
public:
    int equalSubstring(std::string s, std::string t, int maxCost) {
        std::vector<int> diff;
        for (int i = 0; i < s.size(); i++) {
            diff.push_back(s[i] - t[i]);
        }  
        int result = 0, curr = 0, p1 = 0, p2 = 0;
        while (p2 < diff.size()) {
            curr += diff[p2];
            if (curr <= maxCost) {
                result = std::max(result, p2 - p1 + 1);
            }
            while (curr > maxCost) {
                curr -= diff[p1];
                p1++;
            }
            p2++;
        }
        return result;
    }
};