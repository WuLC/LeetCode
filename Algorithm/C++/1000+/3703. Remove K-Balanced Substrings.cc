#include <vector>
#include <string>

class Solution {
public:
    std::string removeSubstring(std::string s, int k) {
        std::vector<char> stack;
        for (char c : s) {
            int n = stack.size();
            if (c == ')' && n >= 2*k-1
                && _equal(stack, n-k+1, n-1, ')')
                && _equal(stack, n-k*2+1, n-k, '(')) {
                    for (int _i = 0; _i < 2*k-1; _i++) stack.pop_back();
                }
            else {
                stack.push_back(c);
            }
        }
        
        std::string result(stack.begin(), stack.end());
        return result;
    }

private:
    bool _equal(std::vector<char>& v, int start, int end, char c) {
        for(int i = start; i <= end ; i++) {
            if (v[i] != c) return false;
        }
        return true;
    }
};

