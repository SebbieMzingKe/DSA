package main

import (
	"fmt"
	"strings"
)

func checkOnesSegment(s string) bool {
	return !strings.Contains(s, "01")
}

func runTest(caseNum int, s string, expected bool) {
	result := checkOnesSegment(s)

	status := "FAIL"
	if result == expected {
		status = "PASS"
	}

	fmt.Printf("Test Case %d: '%s' -> %v (Expected: %v) -> %s\n",
		caseNum, s, result, expected, status)
}

func main() {
	runTest(1, "1001", false)
	runTest(2, "110", true)
	runTest(3, "1", true)
	runTest(4, "1111", true)
	runTest(5, "100000001000", false)
}