/*
 * Created on Mon Dec 24 2018 13:55:17
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

func repeatedNTimes(A []int) int {
	count := make(map[int]int)
	for _, num := range A {
		if count[num] > 0 {
			return num
		}
		count[num] = 1
	}
	return -1
}