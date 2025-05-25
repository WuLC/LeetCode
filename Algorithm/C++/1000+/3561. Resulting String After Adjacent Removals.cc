#include <string>
#include <stack>

class Solution {
public:
    std::string resultingString(std::string s) {
        std::stack<int> indices;
        for(int i=0; i < s.size(); i++) {
            if (!indices.empty()) {
                int diff = abs(s[i] - s[indices.top()]);
                if (diff == 1 || diff == 25) {
                    indices.pop();
                } else {
                    indices.push(i);
                }
            } else {
                indices.push(i);              
            }
        }
        std::string rs;
        rs.reserve(indices.size());
        while (!indices.empty()) {
            rs += s[indices.top()];
            indices.pop();
        }
        return std::string(rs.rbegin(), rs.rend());
    }
};