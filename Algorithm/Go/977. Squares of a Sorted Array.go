/*
 * Created on Mon Jan 21 2019 22:52:12
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

 // two pointers, O(n) time, O(n) space
func abs(num int) int {
	if num <= 0 {
		return -1 * num
	} else {
		return num
	}
}

func sortedSquares(A []int) []int {
	idx := len(A)
	for i, num := range A {
		if num >= 0 {
			idx = i
			break
		}
	}
	result := []int{}
	left, right := idx - 1, idx
	for left>=0 && right<len(A) {
		if (abs(A[left]) > abs(A[right])) {
			result = append(result, A[right]*A[right])
			right++
		} else {
			result = append(result, A[left]*A[left])
			left--		
		}
	}
	for left>=0 {
		result = append(result, A[left]*A[left])
		left--		
	}
	for right<len(A) {
		result = append(result, A[right]*A[right])
		right++		
	}
	return result
}