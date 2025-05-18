#include <vector>
#include <string>

class Solution {
    public:
        int minSwaps(std::vector<int>& nums) {
            int n = nums.size();
            std::vector<std::vector<int>> digitSum(n, std::vector<int>());
            for (int i = 0; i < n; i++) {
                digitSum[i] = std::vector<int>{getDigitSum(nums[i]), nums[i], i};
            }
            sort(digitSum.begin(), digitSum.end(), [](const std::vector<int>& v1, std::vector<int>& v2) {
                if (v1[0] != v2[0]) {
                    return v1[0] < v2[0];
                } else {
                    return v1[1] < v2[1];
                }
            });

            int result = 0;
            for (int i = 0; i < n; i++) {
                while (digitSum[i][2] != i) {
                    result++;
                    swap(digitSum[i], digitSum[digitSum[i][2]]);
                }
            }
            return result;
        }
    
    private:
        int getDigitSum(int num) {
            std::string s = std::to_string(num);
            int result = 0;
            for (char c: s) {
                result += c - '0';
            } 
            return result;
        }
    };