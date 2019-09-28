import "sort"

type UnionFindSet struct {
	parent []int
	depth  []int
}

func (ufs *UnionFindSet) init(n int) {
	for i := 0; i < n; i++ {
		ufs.parent = append(ufs.parent, i)
		ufs.depth = append(ufs.depth, 0)
	}
}

func (ufs *UnionFindSet) findParent(v int) int {
	if ufs.parent[v] != v {
		ufs.parent[v] = ufs.findParent(ufs.parent[v])
	}
	return ufs.parent[v]
}

func (ufs *UnionFindSet) union(v1, v2 int) {
	p1, p2 := ufs.findParent(v1), ufs.findParent(v2)
	if p1 == p2 {
		return
	}
	if ufs.depth[p1] > ufs.depth[p2] {
		ufs.parent[p2] = p1
	} else if ufs.depth[p1] < ufs.depth[p2] {
		ufs.parent[p1] = p2
	} else {
		ufs.parent[p2] = p1
		ufs.depth[p1] += 1
	}
}

// make slice of rune able to sort
type RuneSlice []rune

func (p RuneSlice) Len() int           { return len(p) }
func (p RuneSlice) Less(i, j int) bool { return p[i] < p[j] }
func (p RuneSlice) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }

func smallestStringWithSwaps(s string, pairs [][]int) string {
	n := len(s)
	ufs := UnionFindSet{}
	ufs.init(n)
	for _, p := range pairs {
		ufs.union(p[0], p[1])
	}
	idxs, chars := make(map[int][]int), make(map[int][]rune)
	result := []rune{}
	for i, c := range s {
		p := ufs.findParent(i)
		if _, exist := idxs[p]; !exist {
			idxs[p] = []int{}
		}
		idxs[p] = append(idxs[p], i)
		if _, exist := chars[p]; !exist {
			chars[p] = []rune{}
		}
		chars[p] = append(chars[p], c)
		result = append(result, c)
	}
	for k := range idxs {
		sort.Sort(RuneSlice(chars[k]))
		for i, j := range idxs[k] {
			result[j] = chars[k][i]
		}
	}
	return string(result)

}