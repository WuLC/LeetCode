#include <string>
#include <vector>
#include <cctype>
#include <algorithm>

class Solution {
public:
    std::string processStr(const std::string& s) {
        std::vector<char> result;
        for (char c : s) {
            if (std::isalpha(c)) {
                result.push_back(c);
            } else if (c == '*' && !result.empty()) {
                result.pop_back();
            } else if (c == '#') {
                result.insert(result.end(), result.begin(), result.end());
            } else if (c == '%') {
                std::reverse(result.begin(), result.end());
            }
        }
        return std::string(result.begin(), result.end());
    }
};