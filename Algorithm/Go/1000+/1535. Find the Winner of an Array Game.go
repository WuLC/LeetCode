func getWinner(arr []int, k int) int {
	cnt, idx, curr_num := 0, 1, arr[0]
	for idx < len(arr) {
		if curr_num < arr[idx] {
			cnt = 1
			curr_num = arr[idx]
		} else {
			cnt++
		}
		if cnt == k {
			break
		}
		idx++
	}
	return curr_num
}