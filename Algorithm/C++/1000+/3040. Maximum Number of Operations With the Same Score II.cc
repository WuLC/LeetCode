#include <vector>
#include <tuple>
#include <unordered_map>

class Solution {
public:
    int maxOperations(std::vector<int>& nums) {
        int n = nums.size();
        std::vector<std::vector<int>> memo1(n, vector<int>(n, -1));
        std::vector<std::vector<int>> memo2(n, vector<int>(n, -1));
        std::vector<std::vector<int>> memo3(n, vector<int>(n, -1));
        return 1 + std::max({
                    dfs(0, n-3, nums[n-2]+nums[n-1], nums, memo1),
                    dfs(1, n-2, nums[0]+nums[n-1], nums, memo2),
                    dfs(2, n-1, nums[0]+nums[1], nums, memo3)
                });
    }

private:
    int dfs(int i, int j, int sum, std::vector<int>& nums, std::vector<std::vector<int>>& memo) {
        if (i >= j) return 0;
        if(memo[i][j] > 0) return memo[i][j];
        int curr=0;
        if (nums[i] + nums[i+1] == sum) {
            curr = 1+dfs(i+2, j, sum, nums, memo);
        }
        if (nums[i] + nums[j] == sum) {
            curr = std::max(curr, 1+dfs(i+1, j-1, sum, nums, memo));
        }
        if (nums[j-1] + nums[j] == sum) {
            curr = std::max(curr, 1+dfs(i, j-2, sum, nums, memo));
        }
        return memo[i][j]=curr;
    }


};