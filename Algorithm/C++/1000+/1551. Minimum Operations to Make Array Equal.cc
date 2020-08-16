class Solution {
 public:
    int minOperations(int n) {
        int result = 0;
        for(int i=0; i < (n>>1); i++) result += n-2*i-1;
        return result;
    }
};