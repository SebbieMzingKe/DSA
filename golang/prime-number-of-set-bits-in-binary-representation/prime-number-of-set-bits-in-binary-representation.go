package main

import (
	"fmt"
	"math/bits"
)

func countPrimeSetBits(left int, right int) int {
	primes := map[int]bool{
		2: true,
		3: true,
		5: true,
		7: true,
		11: true,
		13: true,
		17: true,
		19: true,
	}

	primeCount := 0

	for i := left; i <= right; i++ {
		setBits := bits.OnesCount(uint(i))

		if primes[setBits] {
			primeCount++
		}
	}

	return primeCount
}



func runTest(testNum int, left int, right int, expected int) {
	result := countPrimeSetBits(left, right)

	status := "FAIL"
	if result == expected {
		status = "PASS"
	}

	fmt.Printf(
		"Test Case %d: Range [%d, %d] -> %d (Expected: %d) -> %s\n",
		testNum, left, right, result, expected, status,
	)
}


func main() {
	runTest(1, 6, 10, 4)
	runTest(2, 10, 15, 5)
	runTest(3, 21, 21, 1)
	runTest(4, 8, 8, 0)
}