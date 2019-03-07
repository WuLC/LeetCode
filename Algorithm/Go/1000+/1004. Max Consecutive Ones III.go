/*
 * Created on Thu Mar 07 2019 17:1:16
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

//two pointers, O(n) time, O(1) space
func longestOnes(A []int, K int) int {
	left, right, result := 0, 0, 0
	for right < len(A) {
		if A[right] == 0 {
			K--
		}
		for K < 0 {
			if A[left] == 0 {
				K++
			}
			left++
		}
		result = max(right-left+1, result)
		right++
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