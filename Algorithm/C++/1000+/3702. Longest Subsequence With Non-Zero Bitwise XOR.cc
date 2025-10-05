#include <vector>

class Solution {
public:
    int longestSubsequence(std::vector<int>& nums) {
        int xor_res = 0;
        bool has_non_zero = false;
        for (int num: nums) {
            xor_res ^= num;
            if (num > 0) has_non_zero = true;
        }

        if (xor_res != 0) {
            return nums.size();
        } else {
            return has_non_zero? nums.size() - 1: 0;
        }
        
    }
};