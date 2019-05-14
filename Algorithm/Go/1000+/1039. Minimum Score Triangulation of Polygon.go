/*
 * Created on Tue May 14 2019 19:56:6
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


 // recursive
func minScoreTriangulation(A []int) int {
	n := len(A)
	dp := make([][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]int, n)
	}
	return helper(A, 0, n-1, dp)
}


func helper(A []int, i int, j int, dp [][]int) int {
	for k := i+1; k < j; k++ {
		if dp[i][k] == 0 {
			dp[i][k] = helper(A, i, k, dp)
		}
		if dp[k][j] == 0 {
			dp[k][j] = helper(A, k, j, dp)
		}
		tmp := dp[i][k] + A[i] * A[j] * A[k] + dp[k][j]
		if dp[i][j] == 0 {
			dp[i][j] = tmp
		} else {
			dp[i][j] = min(dp[i][j], tmp)
		}
	}
	return dp[i][j]
}


func min(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}