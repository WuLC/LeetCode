#include <vector>
#include <unordered_map>

class Solution {
public:
    int numEquivDominoPairs(std::vector<std::vector<int>>& dominoes) {
        int result=0, tmp;
        std::unordered_map<int, int> counter;
        for(auto d: dominoes) {
            tmp = std::min(d[0], d[1])*10 + std::max(d[0], d[1]);
            if (counter.find(tmp) != counter.end()) {
                result += counter[tmp];
                counter[tmp]++;
            } else {
                counter[tmp] = 1;
            }
        }
        return result;
    }
};