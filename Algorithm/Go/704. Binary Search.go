/*
 * Created on Thu Dec 20 2018 16:20:57
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */
package main

func search(nums []int, target int) int {
	left, right := 0, len(nums)-1
	for left <= right {
		mid := left + ((right - left) >> 1)
		if nums[mid] == target {
			return mid
		} else if nums[mid] > target {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return -1
}
