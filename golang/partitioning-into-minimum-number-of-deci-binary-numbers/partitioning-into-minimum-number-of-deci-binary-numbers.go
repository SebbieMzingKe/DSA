package main

import (
	"fmt"
)

func minPartitions(n string) int {
	maxDigit := 0

	for _, char := range n {
		digit := int(char - '0')

		if digit > maxDigit {
			maxDigit = digit
		}
	}

	return maxDigit
}

func runTest(caseNum int, n string, expected int) {
	result := minPartitions(n)
	status := "FAIL"
	if result == expected {
		status = "PASS"
	}

	fmt.Printf("Test Case %d:\n", caseNum)
	fmt.Printf("  Input:    %s\n", n)
	fmt.Printf("  Output:   %d\n", result)
	fmt.Printf("  Expected: %d\n", expected)
	fmt.Printf("  Status:   %s\n\n", status)
}

func main() {
	runTest(1, "32", 3)
	runTest(2, "82734", 8)
	runTest(3, "27346209830709182346", 9)
	runTest(4, "55555", 5)
	runTest(5, "1", 1)
}