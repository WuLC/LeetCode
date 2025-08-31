class Solution {
    public:
        long long flowerGame(int n, int m) {
            return static_cast<long long>(n>>1)*((m>>1)+(m&1)) + static_cast<long long>(m>>1)*((n>>1)+(n&1));
            // 将任意一个数转为long long 后，与 int 相乘会默认转为 long long 而不会溢出
        }
    };