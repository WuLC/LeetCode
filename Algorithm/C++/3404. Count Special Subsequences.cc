#include <vector>
#include <unordered_map>
#include <numeric>

class Solution {
public:
    long long numberOfSubsequences(std::vector<int>& nums) {
        std::unordered_map<std::string, long long> prefix;
        int n = nums.size();
        long long result = 0;
        for (int q = 2; q < n; q++) {
            for (int p = q-2; p >= 0; p--) {
                int _gcd = std::gcd(nums[p], nums[q]);
                prefix[std::to_string(nums[p]/_gcd)+"/"+std::to_string(nums[q]/_gcd)]++;
            }

            int r = q+2;
            for (int s = r+2; s < n; s++) {
                int _gcd = std::gcd(nums[r], nums[s]);
                result += prefix[std::to_string(nums[s]/_gcd)+"/"+std::to_string(nums[r]/_gcd)];
            }
        }
        return result;
    }
};