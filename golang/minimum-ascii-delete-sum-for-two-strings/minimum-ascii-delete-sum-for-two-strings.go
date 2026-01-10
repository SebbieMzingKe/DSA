package main

import "fmt"

func minimumDeleteSum(s1 string, s2 string) int {
	m, n := len(s1), len(s2)

	dp := make([][]int, m+1)

	for i := range dp {
		dp[i] = make([]int, n+1)
	}

	for i := 1; i <= m; i++ {
		dp[i][0] = dp[i-1][0] + int(s1[i-1])
	}

	for j := 1; j <= n; j++ {
		dp[0][j] = dp[0][j-1] + int(s2[j-1])
	}

	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			if s1[i-1] == s2[j-1] {
				dp[i][j] = dp[i-1][j-1]
			} else {
				deleteS1 := dp[i-1][j] + int(s1[i-1])
				deleteS2 := dp[i][j-1] + int(s2[j-1])
				dp[i][j] = min(deleteS1, deleteS2)
			}
		}
	}

	return dp[m][n]
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func runTest(testNum int, s1, s2 string, expected int) {
	result := minimumDeleteSum(s1, s2)

	status := "FAIL"
	if result == expected {
		status = "PASS"
	}

	fmt.Printf(
		"Test Case %d: '%s', '%s' -> %d (Expected: %d) -> %s\n",
		testNum, s1, s2, result, expected, status,
	)
}

func main() {
	// Example 1
	runTest(1, "sea", "eat", 231)

	// Example 2
	runTest(2, "delete", "leet", 403)

	// Edge Case: identical strings
	runTest(3, "hello", "hello", 0)
}
