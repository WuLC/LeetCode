class Solution {
  public:
    int maxArea(int h, int w, vector<int>& horizontalCuts, vector<int>& verticalCuts) {
        horizontalCuts.push_back(0);
        horizontalCuts.push_back(h);
        verticalCuts.push_back(0);
        verticalCuts.push_back(w);
        std::sort(horizontalCuts.begin(), horizontalCuts.end());
        std::sort(verticalCuts.begin(), verticalCuts.end());
        return (long)maxLen(horizontalCuts)*maxLen(verticalCuts) % long(std::pow(10, 9) + 7);
    }
    
    int maxLen(vector<int>& nums) {
        int result = 0;
        for (int i=1; i<nums.size(); i++) {
            result = std::max(result, nums[i] - nums[i-1]);
        }
        return result;
    }
};