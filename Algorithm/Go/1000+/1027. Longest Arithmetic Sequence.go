/*
 * Created on Tue Apr 16 2019 13:2:27
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// two dimensional dp, O(n^2) time
// dp[i][j] represents the result ending at index i with diff j


func longestArithSeqLength(A []int) int {
	dp := make(map[int]map[int]int)
	result := 0
	for i := 0; i < len(A); i++ {
		dp[i] = make(map[int]int)
		for j := 0; j < i; j++ {
			diff := A[i] - A[j]
			dp[i][diff] = max(dp[i][diff], dp[j][diff] + 1)
			result = max(result, dp[i][diff])
		}
	}
	return result + 1
}

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}