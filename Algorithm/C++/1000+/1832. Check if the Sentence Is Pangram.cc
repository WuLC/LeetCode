#include <unordered_set>
class Solution {
public:
    bool checkIfPangram(string sentence) {
        std::unordered_set<char> s;
        for (char c : sentence) {
            s.insert(c);
        }
        return s.size() == 26;
    }
};