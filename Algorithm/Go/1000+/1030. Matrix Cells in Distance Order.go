/*
 * Created on Tue Apr 23 2019 22:16:12
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// bfs
func allCellsDistOrder(R int, C int, r0 int, c0 int) [][]int {
	queue, result := [][]int{}, [][]int{}
	visited := make(map[int]map[int]bool)
    for i := 0; i < R; i++ {
        visited[i] = make(map[int]bool)
    }
    visited[r0][c0] = true
	queue = append(queue, []int{r0, c0})
	for len(queue) > 0 {
		r, c := queue[0][0], queue[0][1]
		result = append(result, []int{r, c})
		queue = queue[1:]
		if r-1 >= 0 && !visited[r-1][c] {
			queue = append(queue, []int{r-1, c})
			visited[r-1][c] = true
		}
		if r+1 < R && !visited[r+1][c] {
			queue = append(queue, []int{r+1, c})
			visited[r+1][c] = true
		}
		if c-1 >= 0 && !visited[r][c-1] {
			queue = append(queue, []int{r, c-1})
			visited[r][c-1] = true
		}
		if c+1 < C && !visited[r][c+1] {
			queue = append(queue, []int{r, c+1})
			visited[r][c+1] = true
		}
	}
	return result
}