#include <algorithm>
class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        std::sort(costs.begin(), costs.end());
        int result = 0;
        for(int c : costs) {
            if (coins < c) {
                break;
            }
            coins -= c;
            result++;
        }
        return result;
    }
};