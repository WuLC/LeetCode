class Solution {
public:
    int maxIncreasingSubarrays(vector<int>& nums) {
        int pre_len = 0, curr_len = 1;
        int result = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] > nums[i-1]) {
                curr_len++;
            } else {
                pre_len = curr_len;
                curr_len = 1;
            }
            result = std::max(result, std::max(curr_len/2, std::min(curr_len, pre_len)));
        }
        return result;
    }
};