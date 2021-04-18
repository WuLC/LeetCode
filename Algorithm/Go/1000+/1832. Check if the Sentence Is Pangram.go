func checkIfPangram(sentence string) bool {
    s := make(map[rune]bool)
    for _, c := range sentence {
        s[c] = true
    }
    return len(s) == 26
}