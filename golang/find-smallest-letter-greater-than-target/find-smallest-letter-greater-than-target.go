package main

import (
	"fmt"
	"sort"
)

func nextGreatestLetter(letters []byte, target byte) byte {
	n := len(letters)

	index := sort.Search(n, func(i int) bool {
		return letters[i] > target
	})

	return  letters[index % n]
}

func runTest(testNum int, letters []byte, target byte, expected byte) {
	result := nextGreatestLetter(letters, target)

	status := "FAIL"
	if result == expected {
		status = "PASS"
	}

	fmt.Printf(
		"Test Case %d: letters=%v, target='%c' -> Output='%c' (Expected='%c') -> %s\n",
		testNum, letters, target, result, expected, status,
	)
}

func main() {
		// Example 1
	runTest(1, []byte{'c', 'f', 'j'}, 'a', 'c')

	// Example 2
	runTest(2, []byte{'c', 'f', 'j'}, 'c', 'f')

	// Example 3 (Wrap Around)
	runTest(3, []byte{'x', 'x', 'y', 'y'}, 'z', 'x')

	// Edge Case: target smaller than all
	runTest(4, []byte{'a', 'b', 'c'}, '@', 'a')
}