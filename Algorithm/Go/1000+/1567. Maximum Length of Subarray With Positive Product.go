func getMaxLen(nums []int) int {
	left, right, result := 0, 0, 0
	counter := map[int]int{1: 0, -1: 0}
	n := len(nums)
	for right < len(nums) || left < right{
		if (right < n && sign(nums[right]) == 0) ||
		   (right == n && left < right) {
			for left < right {
				if counter[-1]%2 == 0 {
					result = max(result, right-left)
				}
				counter[sigh(nums[left])]--
				left++
			}
			if (right < n) {
				left = right = right + 1
				continue
			}
		}
		if right < n {
			counter[sr]++
			if counter[-1]%2 == 0 {
				result = max(result, right-left+1)
			}
			right++
		}
	}
	return result
}

func sign(num int) int {
	if num == 0 {
		return 0
	} else if num > 0 {
		return 1
	} else {
		return -1
	}
}

func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}