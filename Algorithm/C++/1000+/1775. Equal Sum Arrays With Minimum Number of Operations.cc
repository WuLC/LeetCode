#include <vector>
#include <numeric>
#include <algorithm>

class Solution {
public:
    int minOperations(std::vector<int>& nums1, std::vector<int>& nums2) {
        int n1 = nums1.size(), n2 = nums2.size();
        if (6*n1 < n2 || 6*n2 < n1) return -1; // impossible case

        int result = 0;
        std::sort(nums1.begin(), nums1.end());
        std::sort(nums2.begin(), nums2.end());
        int64_t sum1 = std::accumulate(nums1.begin(), nums1.end(), 0);
        int64_t sum2 = std::accumulate(nums2.begin(), nums2.end(), 0);
        int64_t diff = sum2 - sum1;
        if (diff < 0) {
            // make sure sum2 >= sum1
            std::swap(nums1, nums2);
            std::swap(n1, n2);
            diff *= -1;
        }

        int idx1 = 0, idx2 = n2 - 1, diff1 = 0, diff2 = 0;
        while (diff > 0) {
            diff1 = 6 - nums1[idx1];
            diff2 = nums2[idx2] - 1;
            if (diff1 > diff2) {
                diff -= diff1;
                idx1 += 1;
            } else {
                diff -= diff2;
                idx2 -= 1;
            }
            result += 1;
        }
        return result;
    }
};