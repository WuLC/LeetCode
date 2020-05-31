import (
	"math"
	"sort"
)

func maxArea(h int, w int, horizontalCuts []int, verticalCuts []int) int {
	horizon_nums := append(horizontalCuts, []int{0, h}...)
	vertical_nums := append(verticalCuts, []int{0, w}...)
	sort.Slice(horizon_nums, func(i, j int) bool {
		return horizon_nums[i] < horizon_nums[j]
	})
	sort.Slice(vertical_nums, func(i, j int) bool 
		return vertical_nums[i] < vertical_nums[j]
	})
	return (max_len(horizon_nums) * max_len(vertical_nums)) % int((math.Pow10(9) + 7))
}

func max_len(nums []int) int {
	result := 0
	for i, num := range nums {
		if i > 0 && num-nums[i-1] > result {
			result = num - nums[i-1]
		}
	}
	return result
}