package main

import (
	"fmt"
	"reflect"
)

func minimumDeletions(s string) int {
	bCount := 0
	minDeletions := 0

	for _, char := range s {
		if char == 'b' {
			bCount++
		} else {
			if minDeletions+1 < bCount {
				minDeletions = minDeletions + 1
			} else {
				minDeletions = bCount
			}
		}
	}
	return minDeletions
}

func runTest(testNum int, s string, expected int) {
	result := minimumDeletions(s)

	status := "FAIL"
	if reflect.DeepEqual(result, expected) {
		status = "PASS"
	}

	fmt.Printf(
		"Test Case %d: '%s' -> %d (Expected: %d) -> %s\n",
		testNum, s, result, expected, status,
	)
}

func main() {
	runTest(1, "aababbab", 2)
	runTest(2, "bbaaaaabb", 2)
	runTest(3, "aaabbb", 0)
	runTest(4, "bbbaaa", 3)
}
