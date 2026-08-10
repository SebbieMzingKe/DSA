package main

import "fmt"

type Solution struct{}

func (s Solution) validSequence(word1 string, word2 string) []int {
	n := len(word1)
	m := len(word2)

	suf := make([]int, n+1)

	j := m - 1
	for i := n - 1; i >= 0; i-- {
		if j >= 0 && word1[i] == word2[j] {
			j--
		}
		suf[i] = m - 1 - j
	}

	ans := make([]int, 0, m)
	j = 0
	changed := false

	for i := 0; i < n; i++ {
		if j == m {
			break
		}

		if word1[i] == word2[j] {
			ans = append(ans, i)
			j++
		} else if !changed && suf[i+1] >= m-1-j {
			ans = append(ans, i)
			j++
			changed = true
		}
	}

	if len(ans) == m {
		return ans
	}
	return []int{}
}

func main() {
	solver := Solution{}

	runTest := func(caseNum int, word1, word2 string, expected []int) {
		result := solver.validSequence(word1, word2)

		status := "PASS"
		if !equalSlices(result, expected) {
			status = "FAIL"
		}

		fmt.Printf("Test Case %d:\n", caseNum)
		fmt.Printf("  Input:    word1 = '%s', word2 = '%s'\n", word1, word2)
		fmt.Printf("  Output:   %v\n", result)
		fmt.Printf("  Expected: %v\n", expected)
		fmt.Printf("  Status:   %s\n\n", status)
	}

	runTest(1, "vbcca", "abc", []int{0, 1, 2})
	runTest(2, "bacdc", "abc", []int{1, 2, 4})
	runTest(3, "aaaaaa", "aaabc", []int{})
	runTest(4, "abc", "ab", []int{0, 1})
	runTest(5, "abcdex", "abcdey", []int{0, 1, 2, 3, 4, 5})
}

func equalSlices(a, b []int) bool {
	if len(a) != len(b) {
		return  false
	}

	for i := range a {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}
