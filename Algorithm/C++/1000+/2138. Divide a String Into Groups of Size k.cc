#include <vector>
#include <string>

class Solution {
    public:
        std::vector<std::string> divideString(std::string s, int k, char fill) {
            int fill_cnt = (k - (s.size()%k)) % k;
            s += std::string(fill_cnt, fill);
            std::vector<std::string> result;
            for (int i = 0; i < s.size(); i+=k) {
                result.push_back(s.substr(i, k));
            }
            return result;
        }
    };