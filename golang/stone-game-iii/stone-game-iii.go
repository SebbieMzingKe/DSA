package main

import (
	"fmt"
	"math"
)

func stoneGameIII(stoneValue []int) string {
	n := len(stoneValue)

	dp := make([]int, n+1)
	for i := 0; i < n; i++ {
		dp[i] = math.MinInt32
	}
	dp[n] = 0

	for i := n - 1; i >= 0; i-- {
		takeSum := 0

		for k := 1; k <= 3 && i+k <= n; k++ {
			takeSum += stoneValue[i+k-1]

			score := takeSum - dp[i+k]
			if score > dp[i] {
				dp[i] = score
			}
		}
	}

	if dp[0] > 0 {
		return "Alice"
	}
	if dp[0] < 0 {
		return "Bob"
	}
	return "Tie"
}

func runTest(testNum int, stoneValue []int, expected string) {
	result := stoneGameIII(stoneValue)

	status := "FAIL"
	if result == expected {
		status = "PASS"
	}

	fmt.Printf("Test Case %d:\n", testNum)
	fmt.Printf("  Input:    %v\n", stoneValue)
	fmt.Printf("  Output:   %s\n", result)
	fmt.Printf("  Expected: %s\n", expected)
	fmt.Printf("  Status:   %s\n\n", status)
}

func main() {
	// Example 1
	runTest(1, []int{1, 2, 3, 7}, "Bob")

	// Example 2
	runTest(2, []int{1, 2, 3, -9}, "Alice")

	// Example 3
	runTest(3, []int{1, 2, 3, 6}, "Tie")

	// Custom Case
	runTest(4, []int{-1, -2, -3}, "Tie")
}