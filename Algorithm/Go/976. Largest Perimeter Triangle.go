/*
 * Created on Thu Jan 17 2019 9:43:52
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// a triangle is legal if sum of any two edges is larger than the third one
import "sort"

func largestPerimeter(A []int) int {
	sort.Ints(A)
	result := 0
	for i := len(A) - 1; i > 1; i-- {
		if A[i-1]+A[i-2] > A[i] {
			result = A[i] + A[i-1] + A[i-2]
			break
		}
	}
	return result
}