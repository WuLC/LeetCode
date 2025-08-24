#include <string>
#include <stack>

class Solution {
    public:
        bool canBeValid(std::string s, std::string locked) {
            int n = s.size();
            if (n&1 > 0) return false;

            std::stack<int> left, dynamic;
            for (int i = 0; i < n; i++) {
                if (locked[i] == '0') {
                    dynamic.push(i);
                } else if (s[i] == '(') {
                    left.push(i);
                } else {
                    if (left.size() > 0) {
                        left.pop();
                    } else if (dynamic.size() > 0) {
                        dynamic.pop();
                    } else {
                        return false;
                    }
                }
            }

            while (left.size() > 0 && dynamic.size() > 0 && left.top() < dynamic.top()) {
                left.pop();
                dynamic.pop();
            }

            return left.size() == 0;
        }
    };