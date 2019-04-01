/*
 * Created on Mon Apr 01 2019 9:43:20
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


func numEnclaves(A [][]int) int {
	m, n := len(A), len(A[0])
	for i := 0; i < m; i++ {
		if i == 0 || i == m -1 {
			for j := 0; j < n; j++ {
				if A[i][j] == 1 {
					dfs(A, i, j, m, n)
				}
			}
		} else {
			if A[i][0] == 1 {
				dfs(A, i, 0, m, n)
			}
			if A[i][n-1] == 1{
				dfs(A, i, n-1, m, n)
			}
		}
	}
	result := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			result += A[i][j]
		}
	}
	return result
}


func dfs(A [][]int, i, j, m, n int) {
	A[i][j] = 0
	if i-1 >= 0 && A[i-1][j] == 1 {
		dfs(A, i-1, j, m, n)
	}
	if i+1 < m && A[i+1][j] == 1 {
		dfs(A, i+1, j, m, n)
	}
	if j-1 >= 0 && A[i][j-1] == 1 {
		dfs(A, i, j-1, m, n)
	}
	if j+1 < n && A[i][j+1] == 1 {
		dfs(A, i, j+1, m, n)
	}
}