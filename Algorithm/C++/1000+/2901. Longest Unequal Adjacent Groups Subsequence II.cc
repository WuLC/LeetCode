#include <vector>
#include <string>
class Solution {
    public:
        std::vector<std::string> getWordsInLongestSubsequence(std::vector<std::string>& words, std::vector<int>& groups) {
            int n = words.size();
            std::vector<int> length(n, 1);
            std::vector<std::vector<int>> indices(n, std::vector<int>());

            std::vector<int> record{0, 0};

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < i; j++) {
                    if (groups[i] != groups[j] && isLegalWords(words[i], words[j])) {
                        if (length[i] < length[j] + 1) {
                            indices[i] = std::vector<int>(indices[j].begin(), indices[j].end());
                            length[i] = length[j] + 1;
                        }
                    }
                }
                indices[i].push_back(i);
                if (length[i] > record[0]) {
                    record[0] = length[i];
                    record[1] = i;
                }
            }

            std::vector<std::string> result;
            for (int i: indices[record[1]]) {
                result.push_back(words[i]);
            }
            return result;
        }
    
    private:
        bool isLegalWords(std::string& w1, std::string& w2) {
            if (w1.size() != w2.size()) return false;
            int cnt = 0;
            for (int i = 0; i < w1.size(); i++) {
                if (w1[i] != w2[i]) cnt++;
                if (cnt > 1) break;
            }
            if (cnt == 1) {
                return true;
            } else {
                return false;
            }
        }
    };