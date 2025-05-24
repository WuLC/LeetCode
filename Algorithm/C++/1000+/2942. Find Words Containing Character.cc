#include <vector>

class Solution {
public:
    std::vector<int> findWordsContaining(std::vector<std::string>& words, char x) {
        std::vector<int> result;
        for (int i = 0; i < words.size(); i++) {
            if (contain(words[i], x)) {
                result.push_back(i);
            }
        }
        return result;
    }

private:
    bool contain(std::string& s, char x) {
        for (char c: s) {
            if (c==x) return true;
        }
        return false;
    }
};