#include <string>
#include <stack>
#include <vector>

class Solution {
public:
    std::string clearStars(std::string s) {
        std::vector<std::stack<int>> idx(26, std::stack<int>{});
        std::vector<char> chars;
        chars.reserve(s.size());
        for (int i = 0; i < s.size(); i++) {
            chars.push_back(s[i]);
            if (s[i] == '*') {
                for (int j = 0; j < 26; j++) {
                    if (!idx[j].empty()) {
                        chars[idx[j].top()] = '*';
                        idx[j].pop();
                        break;
                    }
                }
            } else {
                idx[s[i]-'a'].push(i);
            }
        }
        std::string result;
        for (char c: chars) {
            if (c != '*') result += c;
        }
        return result;
    }
};