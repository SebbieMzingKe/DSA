package main

import (
	"fmt"
	"sort"
)

func minimumPushes(word string) int {
	freq := make(map[rune]int)

	for _, ch := range word {
		freq[ch]++
	}

	counts := make([]int, 0, len(freq))

	for _, count := range freq {
		counts = append(counts, count)
	}

	sort.Sort(sort.Reverse(sort.IntSlice(counts)))

	totalPushes := 0

	for i, count := range counts {
		cost := (i / 8) + 1
		totalPushes += count * cost
	}

	return totalPushes
}


func runTest(caseNum int, word string, expected int) {
	result := minimumPushes(word)

	status := "FAIL"
	if result == expected  {
		status = "PASS"
	}

	fmt.Printf("Test Case %d:\n", caseNum)
	fmt.Printf("  Input:    word = %q\n", word)
	fmt.Printf("  Output:   %d\n", result)
	fmt.Printf("  Expected: %d\n", expected)
	fmt.Printf("  Status:   %s\n\n", status)
}

func main() {
	// Example 1
	runTest(1, "abcde", 5)

	// Example 2
	runTest(2, "xyzxyzxyzxyz", 12)

	// Example 3
	runTest(3, "aabbccddeeffgghhiiiiii", 24)

	// Example 4
	runTest(4, "abcdefghijklmnopqrstuvwxyz", 56)
}