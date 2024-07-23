#include <string>
#include <vector>

class Solution {
public:
    int removeAlmostEqualCharacters(std::string word) {
        int n = word.size();
        std::vector<int> remain(n, 0), remove(n, 0);
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                remain[i] = 0;
                remove[i] = 1;
            } else {
                if (std::abs(word[i] - word[i-1]) <= 1) {
                    remain[i] = remove[i-1];
                } else {
                    remain[i] = std::min(remove[i-1], remain[i-1]);
                }
                remove[i] = std::min(remove[i-1], remain[i-1]) + 1;
            }
        }
        return std::min(remain[n-1], remove[n-1]);
    }
};