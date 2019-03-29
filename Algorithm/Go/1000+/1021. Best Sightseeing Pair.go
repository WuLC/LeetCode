/*
 * Created on Fri Mar 29 2019 23:0:32
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// one pass solution, 
// find the max A[i]+i-j from left to right


func maxScoreSightseeingPair(A []int) int {
	result, curr := 0, A[0] - 1
	for i := 1; i < len(A); i++ {
		result = max(result, curr + A[i])
		curr = max(curr - 1, A[i] - 1)
	}
	return result
}

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b 
	}
}