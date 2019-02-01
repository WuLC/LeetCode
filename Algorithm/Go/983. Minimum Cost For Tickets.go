/*
 * Created on Fri Feb 01 2019 9:10:2
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

 // dp, O(n) time, O(n) space
func mincostTickets(days []int, costs []int) int {
	dp := []int{0}
	for i := 0; i < len(days); i++ {
		dp = append(dp, dp[i] + costs[0])
		for j := i-1; j >= 0 && j >= i - 30; j-- {
			if days[j] > days[i] - 7 {
				dp[i+1] = min(dp[i+1], dp[j] + costs[1])
			}
			if days[j] > days[i] - 30 {
				dp[i+1] = min(dp[i+1], dp[j] + costs[2])
			} else {
				break
			}
		}
	}
	return dp[len(dp)-1]
}

func min(A, B int) int {
	if A < B {
		return A
	} else {
		return B
	}
}