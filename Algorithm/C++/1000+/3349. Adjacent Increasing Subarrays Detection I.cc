class Solution {
public:
    bool hasIncreasingSubarrays(vector<int>& nums, int k) {
        int pre_len = 0, curr_len = 1;
        for(int i = 1; i < nums.size(); i++) {
            if (nums[i] > nums[i-1]) {
                curr_len++;
            } else {
                pre_len = curr_len;
                curr_len = 1;
            }
            if ((pre_len >= k && curr_len >= k) || curr_len == 2*k){
                return true;
            }
        }
        return false;
    }
};