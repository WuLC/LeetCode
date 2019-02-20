/*
 * Created on Wed Feb 20 2019 12:16:44
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// greedy, from left to right, flip when metting 0
// two solutions, referer: https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/discuss/239284/C%2B%2B-O(n)-or-O(K)-and-O(n)-or-O(1)
#include <queue>
#include <vector>

using std::queue;
using std::vector;

// solution 1, O(n) time, O(n) space
class Solution {
 public:
  int minKBitFlips(vector<int>& A, int K) {
    int result = 0;
    queue<int> q;
    for (int i = 0; i < A.size(); ++i) {
      if ((A[i] == 0 && (q.size()&1) == 0) || (A[i] == 1 && (q.size()&1) == 1)) {
        result++;
        q.push(i+K-1);
      }
      while (q.size() > 0 && q.front() <= i) q.pop();
    }
    return q.size()==0 ? result : -1; 
  }
};


// solution 2, O(n) time, O(1) space
class Solution {
 public:
  int minKBitFlips(vector<int>& A, int K) {
    int result = 0, flips = 0;
    for (int i = 0; i < A.size(); ++i) {
      if ((A[i] == 0 && (flips&1) == 0) || (A[i] == 1 && (flips&1) == 1)) {
        result++;
        flips++;
        A[i] -= 2;
      }
      if (i-K+1>= 0 && A[i-K+1] < 0) flips--;
    }
    return flips==0 ? result : -1;
  }
};