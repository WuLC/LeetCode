#include <string>
#include <unordered_map>

class Solution {
public:
    int countKConstraintSubstrings(std::string s, int k) {
        int left = 0, right = 0, result = 0;
        int n = s.size();
        std::unordered_map<char, int> counter = { {'0', 0}, {'1', 0} };
        while (right < n) {
            counter[s[right]]++;
            while (counter['0'] > k and counter['1'] > k) {
                counter[s[left]]--;
                left++;
            }
            result += right - left + 1;
            right++;
        }
        return result;
    }
};