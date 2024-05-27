#include <vector>
#include <algorithm>

class Solution {
public:
    int getMaximumConsecutive(std::vector<int>& coins) {
        int curr_sum = 0;
        std::sort(coins.begin(), coins.end());
        for (int i = 0; i < coins.size(); i++) {
            if (curr_sum + 1 < coins[i]) break;
            curr_sum += coins[i];
        }
        return curr_sum+1;
    }
};