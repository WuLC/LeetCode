/*
 * Created on Sat Jan 12 2019 15:11:25
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

func rob(nums []int) int {
	previous, curr := 0, 0
	for _, num := range nums {
		tmp := previous + num
		if tmp < curr {
			tmp = curr
		}
		previous, curr = curr, tmp
	}
	return curr
}