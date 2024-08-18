#include <vector>

class Solution {
public:
    long long maxEnergyBoost(std::vector<int>& energyDrinkA, std::vector<int>& energyDrinkB) {
        int n = energyDrinkA.size();
        std::vector<long long> dpA(n+1, 0), dpB(n+1, 0);
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                dpA[i+1] = energyDrinkA[i];
                dpB[i+1] = energyDrinkB[i];
            } else {
                dpA[i+1] = std::max(dpA[i], dpB[i-1]) + energyDrinkA[i];
                dpB[i+1] = std::max(dpA[i-1], dpB[i]) + energyDrinkB[i];
            }
        }
        return std::max(dpA[n], dpB[n]);
    }
};