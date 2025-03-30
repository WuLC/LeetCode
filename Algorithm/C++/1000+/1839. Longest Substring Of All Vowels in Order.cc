#include <string>
#include <unordered_set>

class Solution {
public:
    int longestBeautifulSubstring(string word) {
        int left, idx = 0, n = word.size();
        std::unordered_set<char> cand;
        int result = 0;
        while(idx < n) {
            if (word[idx] == 'a' && cand.size() == 0) {
                left = idx;
                cand.insert(word[idx]);
            }
            bool valid = true;
            for (auto c: cand) {
                valid &= (word[idx] >= c);
            }
            if (valid) {
                cand.insert(word[idx]);
                if (word[idx] == 'u' && cand.size() == 5) {
                    result = std::max(result, idx - left + 1);
                }
            } else {
                cand.clear();
                continue;
            }
            idx++;
        }
        return result;        
    }
};