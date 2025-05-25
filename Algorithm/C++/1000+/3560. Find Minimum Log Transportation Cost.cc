class Solution {
    public:
        long long minCuttingCost(int n, int m, int k) {
            long long result = 0;
            if (n > k) result += static_cast<long long>(k) * static_cast<long long>(n-k);
            if (m > k) result += static_cast<long long>(k) * static_cast<long long>(m-k);
            return result;
        }
    };