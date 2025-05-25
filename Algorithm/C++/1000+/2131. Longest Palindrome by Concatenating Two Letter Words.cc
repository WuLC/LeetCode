#include <vector>
#include <string>
#include <unordered_map>

class Solution {
    public:
        int longestPalindrome(std::vector<std::string>& words) {
            std::unordered_map<std::string, int> record;
            int count = 0;
            for (auto w: words) {
                std::string rw(w.rbegin(), w.rend());
                if (record.find(rw) != record.end()) {
                    record[rw] -= 1;
                    count += 2;
                } else {
                    record[w]++;
                }
            }
            for (const auto& pair: record) {
                if (pair.second > 0 && pair.first[0] == p.first[1]) {
                    count++;
                    break
                }
            }
            return count<<1;
        }
    };