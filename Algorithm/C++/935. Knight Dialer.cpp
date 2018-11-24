/*
 * Created on Mon Nov 12 2018 16:58:33
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// dp
class Solution {
 public:
    int knightDialer(int N) {
      vector<int> pre(10), curr(10, 1);
      int mod = 1000000007;
      while (N > 1) {
        std::swap(pre, curr);
        curr[0] = (pre[4] + pre[6]) % mod;
        curr[1] = (pre[6] + pre[8]) % mod;
        curr[2] = (pre[7] + pre[9]) % mod;
        curr[3] = (pre[4] + pre[8]) % mod;
        curr[4] = (pre[0] + pre[3] + pre[9]) % mod;
        curr[5] = 0;
        curr[6] = (pre[0] + pre[1] + pre[7]) % mod;
        curr[7] = (pre[2] + pre[6]) % mod;
        curr[8] = (pre[1] + pre[3]) % mod;
        curr[9] = (pre[2] + pre[4]) % mod;
        N--;
      }
      return std::accumulate(curr.begin(), curr.end(), 0) % mod;
    }
};

// idea same as the above code, AC
class Solution {
 public:
  int knightDialer(int N) {
    vector<vector<int>> ms = { {4, 6}, {6, 8}, {7, 9}, {4, 8}, {3, 9, 0}, {}, {1, 7, 0}, {2, 6}, {1, 3}, {4, 2}};
    int knightDialer(int N) {
    vector<int> d1(10, 1), d2(10);
    for (; --N > 0; swap(d1, d2))
      for (auto i = 0; i < d1.size(); ++i) 
          d2[i] = accumulate(begin(ms[i]), end(ms[i]), 0, [&](int s, int i) {return (s + d1[i]) % 1000000007;});
    return accumulate(begin(d1), end(d1), 0, [](int s, int n) {return (s + n) % 1000000007;});
    }
  }
}
