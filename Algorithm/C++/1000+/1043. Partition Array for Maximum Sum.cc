#include <vector>
#include <algorithm>

class Solution {
public:
    int maxSumAfterPartitioning(std::vector<int>& arr, int k) {
        int n = arr.size();
        std::vector<int> dp(n+1, 0);
        for (int i = 0; i < n; i++) {
            int offset = 0, _max = arr[i];
            while (offset < k && i-offset >= 0) {
                _max = std::max(_max, arr[i-offset]);
                dp[i+1] = std::max(dp[i+1], dp[i-offset] + _max*(offset+1));
                offset++;
            }
        }
        return dp[n];
    }
};