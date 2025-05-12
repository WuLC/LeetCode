#include <vector>

class Solution {
    public:
        long long minSum(std::vector<int>& nums1, std::vector<int>& nums2) {
            std::vector<long long> zeros_sum1(2, 0), zeros_sum2(2, 0);
            get_zeros_and_sum(nums1, zeros_sum1);
            get_zeros_and_sum(nums2, zeros_sum2);
            long long zeros1 = zeros_sum1[0], sum1 = zeros_sum1[1], zeros2 = zeros_sum2[0], sum2 = zeros_sum2[1]; 
            if ((zeros1 == 0 && sum1 - sum2 < zeros2) || (zeros2 == 0 && sum2 - sum1 < zeros1)) {
                return -1;
            }
            return std::max(sum1 + zeros1, sum2 + zeros2);
        }
    
    private:
        void get_zeros_and_sum(std::vector<int>& nums, std::vector<long long>& zeros_sum) {
            for (auto num: nums) {
                if (num == 0) zeros_sum[0]++;
                zeros_sum[1] += num;
            }
            return;
        }
    
    };