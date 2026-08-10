package main

import "fmt"

func winnerSquareGame(n int) bool {
	dp := make([]bool, n+1)

	squares := make([]int, 0)

	for k := 1; k*k <= n; k++ {
		squares = append(squares, k*k)
	}

	for i := 1; i <= n; i++ {
		for _, sq := range squares {
			if sq > i {
				break
			}

			if !dp[i-sq] {
				dp[i] = true
				break
			}
		}
	}
	return dp[n]
}

func runTest(testNum int, n int, expected bool) {
	result := winnerSquareGame(n)

	status := "FAIL"
	if result == expected {
		status = "PASS"
	}

	fmt.Printf("Test Case %d:\n", testNum)
	fmt.Printf("  Input:    n = %d\n", n)
	fmt.Printf("  Output:   %t\n", result)
	fmt.Printf("  Expected: %t\n", expected)
	fmt.Printf("  Status:   %s\n\n", status)
}

func main() {
	// Example 1
	runTest(1, 1, true)

	// Example 2
	runTest(2, 2, false)

	// Example 3
	runTest(3, 4, true)

	// Custom Case 4: Larger number
	runTest(4, 7, false)

	// Custom Case 5: 17 stones (17 -> 16 -> 1) Alice wins
	runTest(5, 17, true)
}
