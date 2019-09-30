import "strings"

type Stack struct {
	chars []rune
	count []int
}

func (s *Stack) pop() (rune, int) {
	topChar, topCnt := s.chars[len(s.chars)-1], s.count[len(s.count)-1]
	s.chars, s.count = s.chars[:len(s.chars)-1], s.count[:len(s.count)-1]
	return topChar, topCnt
}

func (s *Stack) push(c rune, n int) {
	s.chars = append(s.chars, c)
	s.count = append(s.count, n)
}

func (s *Stack) top() (rune, int) {
	return s.chars[len(s.chars)-1], s.count[len(s.count)-1]
}

func (s *Stack) size() int {
	return len(s.chars)
}

func removeDuplicates(s string, k int) string {
	sta := Stack{}
	for _, c := range s {
		if sta.size() > 0 {
			if char, cnt := sta.top(); char == c {
				sta.pop()
				sta.push(char, cnt+1)
			} else {
				sta.push(c, 1)
			}
		} else {
			sta.push(c, 1)
		}
		_, cnt := sta.top()
		if cnt == k {
			sta.pop()
		}
	}
	var result string
	for sta.size() > 0 {
		char, cnt := sta.pop()
		result = strings.Repeat(string(char), cnt) + result
	}
	return result
}