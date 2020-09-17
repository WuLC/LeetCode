
// Kruskal algorithm, yet TLE
import "sort"

type UnionFindSet struct {
	parent []int
	height []int
}

func newUnionFindSet(n int) *UnionFindSet {
	ufs := UnionFindSet{}
	for i := 0; i < n; i++ {
		ufs.parent = append(ufs.parent, i)
		ufs.height = append(ufs.height, 0)
	}
	return &ufs
}

func (ufs *UnionFindSet) Find(v int) int {
	if v != ufs.parent[v] {
		ufs.parent[v] = ufs.Find(ufs.parent[v])
	}
	return ufs.parent[v]
}

func (ufs *UnionFindSet) Union(p1, p2 int) {
	if ufs.height[p1] == ufs.height[p2] {
		ufs.parent[p2] = p1
		ufs.height[p1]++
	} else if ufs.height[p1] > ufs.height[p2] {
		ufs.parent[p2] = p1
	} else {
		ufs.parent[p1] = p2
	}
}

func minCostConnectPoints(points [][]int) int {
	distance := [][]int{}
	n := len(points)
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			distance = append(distance, []int{i, j, abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])})
		}
	}
	sort.SliceStable(distance, func(i, j int) bool {
		return distance[i][2] < distance[j][2]
	})
	result := 0
	ufs := newUnionFindSet(n)
	for _, d := range distance {
		p1, p2 := ufs.Find(d[0]), ufs.Find(d[1])
		if p1 != p2 {
			result += d[2]
			ufs.Union(p1, p2)
		}
	}
	return result
}

func abs(v int) int {
	if v >= 0 {
		return v
	} else {
		return -v
	}
}