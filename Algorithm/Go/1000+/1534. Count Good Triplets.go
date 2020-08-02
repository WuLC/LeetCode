

func countGoodTriplets(arr []int, a int, b int, c int) int {
	result, n := 0, len(arr)
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if abs(arr[i]-arr[j]) > a {
				continue
			}
			for k := j + 1; k < n; k++ {
				if abs(arr[j]-arr[k]) > b || abs(arr[j]-arr[i]) > c {
					continue
				}
				result++
			}
		}
	}
	return result
}

func abs(num int) int {
	if num >= 0 {
		return num
	} else {
		return num * -1
	}

}