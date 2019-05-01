/*
 * Created on Wed May 01 2019 17:51:24
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

import "sort"


func numMovesStones(a int, b int, c int) []int {
	nums := []int{a, b, c}
	sort.Ints(nums)
	min_move, max_move := 0, 0
	if nums[2] - nums[1] == 2 || nums[1] - nums[0] == 2 {
		min_move = 1
	} else {
		min_move = min(1, nums[2]-nums[1]-1) + min(1, nums[1]-nums[0]-1)
	}
	max_move = nums[2] - nums[0] - 2
	return []int{min_move, max_move}
}


func min(a, b int) int {
	if a < b {
		return a 
	} else {
		return b
	}
}


func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}