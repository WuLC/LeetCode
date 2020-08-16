// two pointers
#include <vector>

class Solution {
 public:
    int maxSum(std::vector<int>& nums1, std::vector<int>& nums2) {
        const int m = nums1.size(), n = nums2.size();
        int idx1 = 0, idx2 = 0;
        uint64_t curr_sum1 = 0, curr_sum2 = 0, mod=1e9+7;
        while (idx1 < m || idx2 < n) {
            if (idx1 < m && (idx2 == n || nums1[idx1] < nums2[idx2])) {
                curr_sum1 += nums1[idx1];
                idx1++;
            } else if (idx2 < n && (idx1 == m || nums1[idx1] > nums2[idx2])) {
                curr_sum2 += nums2[idx2];
                idx2++;
            } else {
                curr_sum1 = curr_sum2 = std::max(curr_sum1, curr_sum2) + nums1[idx1];
                idx1++;
                idx2++;
            }
        }
        return int(std::max(curr_sum1, curr_sum2)%mod);
    }
};