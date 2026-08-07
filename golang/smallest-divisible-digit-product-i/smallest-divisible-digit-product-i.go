#package main

import "fmt"

/func smallestNumber(n int, t int) int {
	digitProduct := func(num int) int {
		product := 1

		for num > 0 {
			product *= num % 10
			num /= 10
		}

		return product
	}

	current := n

	for {
		if digitProduct(current)%t == 0 {
			return current
		}
		current++
	}
}

/func runTest(testNum, n, t, expected int) {
	result := smallestNumber(n, t)

	status := "FAIL"
	if result == expected {
		status = "PASS"
	}

	fmt.Printf("Test Case %d:\n", testNum)
	fmt.Printf("  Input:    n = %d, t = %d\n", n, t)
	fmt.Printf("  Output:   %d\n", result)
	fmt.Printf("  Expected: %d\n", expected)
	fmt.Printf("  Status:   %s\n\n", status)
}

/func main() {
	// Example 1
	runTest(1, 10, 2, 10)

	// Example 2
	runTest(2, 15, 3, 16)

	// Custom Case 3
	runTest(3, 11, 4, 14)

	// Custom Case 4
	runTest(4, 3, 7, 7)
}
