// two pointers
func maxSum(nums1 []int, nums2 []int) int {
	m, n := len(nums1), len(nums2)
	idx1, idx2 := 0, 0
	var curr_sum1, curr_sum2 uint64 = 0, 0
	for idx1 < m || idx2 < n {
		if idx1 < m && (idx2 == n || nums1[idx1] < nums2[idx2]) {
			curr_sum1 += uint64(nums1[idx1])
			idx1++
		} else if idx2 < n && (idx1 == m || nums1[idx1] > nums2[idx2]) {
			curr_sum2 += uint64(nums2[idx2])
			idx2++
		} else {
			tmp := max(curr_sum1, curr_sum2) + uint64(nums1[idx1])
			curr_sum1, curr_sum2 = tmp, tmp
			idx1++
			idx2++
		}
	}
	return int(max(curr_sum1, curr_sum2) % (1e9 + 7))
}

func max(num1, num2 uint64) uint64 {
	if num1 >= num2 {
		return num1
	} else {
		return num2
	}
}