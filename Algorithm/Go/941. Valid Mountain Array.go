/*
 * Created on Sat Nov 24 2018 10:57:8
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// assume two people climb from left and right, judge whether they reach the same peak at last
func validMountainArray(A []int) bool {
	n := len(A)
	var left, right = 0, n - 1
	for left+1 < n && A[left] < A[left+1] {
		left++
	}
	for right-1 >= 0 && A[right] < A[right-1] {
		right--
	}
	return left == right && left != 0 && right != n-1
}