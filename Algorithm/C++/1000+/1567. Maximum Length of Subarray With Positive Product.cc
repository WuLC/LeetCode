#include <vector>
#include <unordered_map>

class Solution {
public:
    int getMaxLen(std::vector<int>& nums) {
        auto sign = [](int a) {return a==0? 0:(a<0? -1: 1);};
        int left = 0, right = 0, result = 0;
        std::unordered_map<int, int> counter({{1, 0}, {-1, 0}});
        int n = nums.size();
        while (right < n || left < right) {
            if ((right < n && sign(nums[right]) == 0) || (right == n && left < right)) {
                while (left < right) {
                   if (counter[-1]%2 == 0) result = std::max(result, right - left);
                   counter[sign(nums[left])]--;
                   left++;
                }
                if (right < n) {
                    left = right = right + 1;
                    continue;
                }
            } 
            if (right < n) {
                counter[sign(nums[right])]++;
                if (counter[-1]%2 == 0) result = std::max(result, right - left + 1);
                right++;
            }
        }
        return result;
    }
};