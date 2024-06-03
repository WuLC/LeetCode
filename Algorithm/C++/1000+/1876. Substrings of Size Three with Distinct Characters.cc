#include <string>
#include <unordered_map>

class Solution {
public:
    int countGoodSubstrings(std::string s) {
        int result = 0;
        std::unordered_map<char, int> counter;
        for (int i=0; i < s.size(); i++) {
            char c = s[i];
            if (counter.find(c) != counter.end()) {
                counter[c]++;
            } else {
                counter[c] = 1;
            }
            if (i > 2) {
                char c1 = s[i-3];
                counter[c1]--;
                if (counter[c1] == 0) {
                    counter.erase(c1);
                }
            }
            if (counter.size() == 3) {
                result++;
            }
        }
        return result;
    }
};