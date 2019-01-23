/*
 * Created on Wed Jan 23 2019 16:20:49
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

 // two pointers, O(n) time
func maxTurbulenceSize(A []int) int {
	result := 1
	left, right := 0, 1
	for right < len(A) - 1 {
		if (A[right]<A[right-1] && A[right]<A[right+1]) || (A[right]>A[right-1] && A[right]>A[right+1]){
			right++
		} else {
			if A[right] != A[right-1] && right-left+1 > result {
				result = right - left + 1
			}
			for right < len(A) - 1 && A[right] == A[right+1] {
				right++
			}
			left, right = right, right+1
		}
	} 
	if right < len(A) && A[right] != A[right-1] && right-left+1 > result {
		result = right - left + 1
	}
	return result
}