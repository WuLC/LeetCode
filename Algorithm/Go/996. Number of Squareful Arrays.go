/*
 * Created on Sun Mar 03 2019 23:31:37
 * Author: WuLC
 * EMail: liangchaowu5@gmail.com
 */

// graph, dfs with counter to deal with duplicate elements

import "math"

type graph struct {
	Conn    map[int]map[int]bool
	Counter map[int]int
	Result  int
}

func (p *graph) dfs(curr int, left int) {
	p.Counter[curr]--
	if left == 0 {
		p.Result++
	}
	for k, _ := range p.Conn[curr] {
		if p.Counter[k] > 0 {
			p.dfs(k, left-1)
		}
	}
	p.Counter[curr]++
}

func numSquarefulPerms(A []int) int {
	g := &graph{map[int]map[int]bool{}, map[int]int{}, 0}
	for i := 0; i < len(A); i++ {
		g.Counter[A[i]]++
		for j := i + 1; j < len(A); j++ {
			if A[i]+A[j] == int(math.Pow(float64(int(math.Sqrt(float64(A[i]+A[j])))), 2.0)) {
				if _, in := g.Conn[A[i]]; !in {
					g.Conn[A[i]] = make(map[int]bool)
				}
				if _, in := g.Conn[A[j]]; !in {
					g.Conn[A[j]] = make(map[int]bool)
				}
				g.Conn[A[i]][A[j]] = true
				g.Conn[A[j]][A[i]] = true
			}
		}
	}
	for k, _ := range g.Conn {
		g.dfs(k, len(A)-1)
	}
	return g.Result
}