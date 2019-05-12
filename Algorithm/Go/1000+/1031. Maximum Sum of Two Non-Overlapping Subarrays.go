/*
 * Created on Sun May 12 2019 17:18:20
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */



// dp, O(n) time
func maxSumTwoNoOverlap(A []int, L int, M int) int {
	return max(helper(A, L, M), helper(A, M, L))
}

func helper(A []int, L int, M int) int {
	n := len(A)
	left, right := make([]int, n+1), make([]int, n+1)
	currLeft, currRight := 0, 0
	for i, j := 0, n-1; i < n; i, j = i+1, j-1 {
		currLeft += A[i]
		currRight += A[j]
		if (i >= L) {
			currLeft -= A[i-L]
		}
		if (j <= n-1-M) {
			currRight -= A[j+M]
		}
		left[i+1] = max(left[i], currLeft)
		right[j] = max(right[j+1], currRight)
	}
	result := 0
	for i := 0; i < n; i++ {
		result = max(result, max(left[i] + right[i], left[i+1] + right[i+1]))
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