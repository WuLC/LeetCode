/*
 * Created on Sun Feb 17 2019 21:6:15
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// bfs, there may be multiple rotton oranges
func orangesRotting(grid [][]int) int {
	queue := [][]int{}
	m, n := len(grid), len(grid[0])
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 2 {
				queue = append(queue, []int{i, j, 0})
			}
		}
	}
	result := 0
	directions := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	for len(queue) > 0 {
		curr := queue[0]
		queue = queue[1:]
		for _, d := range directions {
			ni, nj := curr[0]+d[0], curr[1]+d[1]
			if ni >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] == 1 {
				grid[ni][nj] = 2
				queue = append(queue, []int{ni, nj, curr[2] + 1})
			}
		}
		result = curr[2]
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				return -1
			}
		}
	}
	return result
}