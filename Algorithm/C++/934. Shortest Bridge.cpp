/*
 * Created on Fri Nov 09 2018 22:58:8
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


// bfs
class Solution {
 public:
  int shortestBridge(vector<vector<int>>& A) {
    // initialize the graph
    queue<vector<int>> edges;
    bool painted = false;
    for(int i = 0; i < A.size(); ++i) {
      for(int j = 0; j < A.size(); ++j) {
        if (A[i][j] == 1) {
          paint(A, edges, i, j);
          painted = true;
          break;
        }
      }
      if (painted) break;
    }
      
    // bfs
    bool connected = false;
    vector<int> curr;
    const vector<vector<int>> directions {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    while(edges.size() > 0) {
      curr = edges.front();
      for (auto d : directions) {
        int ci = curr[0] + d[0], cj = curr[1] + d[1];
        if (ci >= 0 && ci < A.size() && cj >= 0 && cj < A.size()) {
          if (A[ci][cj] == 0) {
            A[ci][cj] = A[curr[0]][curr[1]] + 1;
            vector<int> next{ci, cj};
            edges.push(next);
          }
          else if (A[ci][cj] == 1) {
            connected = true;
            break;
          }
        }
      }
      // printVector(A);
      edges.pop();
      if (connected) break;
    }
    return A[curr[0]][curr[1]] - 2;
  }

 private:
  void paint(vector<vector<int>>& A, queue<vector<int>>& edges, int i, int j) {
    if (i < 0 || i >= A.size() || j < 0 || j >= A.size() || A[i][j] != 1) return;
    A[i][j] = 2;
    if ((i - 1 >= 0 && A[i-1][j] == 0) ||
        (i + 1 < A.size() && A[i+1][j] == 0) ||
        (j - 1 >= 0 && A[i][j-1] == 0) ||
        (j + 1 < A.size() && A[i][j+1] == 0)) {
          vector<int> pos {i, j};
          edges.push(pos);
        }
    paint(A, edges, i - 1, j);
    paint(A, edges, i + 1, j);
    paint(A, edges, i, j - 1);
    paint(A, edges, i, j + 1);
  }

  void printVector(vector<vector<int>>& A) {
    for (int i = 0; i < A.size(); i++) {
      for (int j = 0; j < A.size(); j++) {
        cout << A[i][j] << ' ';
      }
      cout << endl;
    }
    cout << endl;
  }
};


