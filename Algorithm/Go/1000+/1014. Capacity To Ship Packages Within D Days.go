/*
 * Created on Thu Mar 21 2019 22:51:36
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */


func shipWithinDays(weights []int, D int) int {
	left, right := 0, 0
	for _, w := range weights {
		left = max(left, w)
		right += w
	}
	mid, tmp, days := 0, 0, 0
	for left < right {
		mid, tmp, days = left + ((right - left) >> 1), 0, 0
		for _, w := range weights {
			if tmp + w > mid {
				days++
				tmp = 0
			}
			tmp += w
		}
		days++
		if days > D {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return right
}

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}