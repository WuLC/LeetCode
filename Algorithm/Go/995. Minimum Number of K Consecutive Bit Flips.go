/*
 * Created on Fri Feb 22 2019 21:51:40
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


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