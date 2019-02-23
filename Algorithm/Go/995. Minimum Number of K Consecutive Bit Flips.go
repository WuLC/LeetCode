/*
 * Created on Fri Feb 22 2019 21:51:40
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// greedy, flip when meeting 0
// O(n) time, O(n) space
func minKBitFlips(A []int, K int) int {
	result, queue := 0, []int{}
	for i, v := range A {
		if (v == 0 && (len(queue)&1) == 0) || (v == 1 && (len(queue)&1) == 1) {
			queue = append(queue, i+K-1)
			result++
		}
		if len(queue) > 0 && queue[0] <= i {
			queue = queue[1:]
		}
	}
	if len(queue) == 0 {
		return result
	} else {
		return -1
	}
}


// O(n) time, O(1) space
func minKBitFlips(A []int, K int) int {
	flips, result := 0, 0
	for i, v := range A {
		if (v == 0 && (flips&1) == 0) || (v == 1 && (flips&1) == 1) {
			flips++
			result++
			A[i] -= 2
		}
		if  i-K+1 >= 0 && A[i-K+1] < 0 {
			flips -= 1
		}
	}
	if flips == 0 {
		return result
	} else {
		return -1
	}
}