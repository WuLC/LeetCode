/*
 * Created on Fri Feb 15 2019 14:4:41
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


 // two pointers
 func subarraysWithKDistinct(A []int, K int) int {
	i, j, prefix, result := 0, 0, 0, 0
	count := make(map[int]int)
	for j < len(A) {
		count[A[j]]++
		j++
		for len(count) > K {
			prefix = 0
			count[A[i]]--
			if count[A[i]] == 0 {
				delete(count, A[i])
			}
			i++
		}
		if len(count) == K {
			result++
			for count[A[i]] > 1 {
				count[A[i]]--
				prefix++
				i++
			}
		}
		result += prefix
	}
	return result
}