#include <vector>

class Solution {
 public:
    std::vector<int> beautifulArray(int N) {
        std::vector<int> result{1};
        while(result.size() < N) {
            std::vector<int> odds, evens;
            for(auto num: result) {
                if (num*2 - 1 <= N) odds.push_back(num*2-1);
                if (num*2 <= N) evens.push_back(num*2);
            }
            odds.insert(odds.end(), evens.begin(), evens.end());
            result=odds;
        }
        return result;
    }
};