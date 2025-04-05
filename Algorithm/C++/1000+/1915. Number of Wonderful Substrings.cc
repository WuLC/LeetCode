#include <string>
#include <unordered_map>

class Solution {
public:
    long long wonderfulSubstrings(std::string word) {
        long long result = 0;
        int n = word.size(), prefix = 0, tmp;
        std::unordered_map<int, int> counter;
        counter[0] = 1;
        for (char c: word) {
            prefix = prefix xor (1 << (c-'a'));
            if (counter.find(prefix) != counter.end()) {
                result += counter[prefix];
                counter[prefix]++;
            } else {
                counter[prefix]=1;
            }
            for (int i=0; i < 10; i++) {
                tmp = prefix xor (1 << i);
                if (counter.find(tmp) != counter.end()) {
                    result += counter[tmp];
                }
            }
        }
        return result;
    }
};