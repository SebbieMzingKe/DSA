package main

import (
	"fmt"
	"reflect"
)

func maxMatrixSum(matrix [][]int) int64 {
	var totalSum int64 = 0
	minAbs := int64(1<<63 - 1)

	negCount := 0

	for _, row := range matrix {
		for _, val := range row {

			if val < 0 {
				// absVal = -absVal
				negCount++
			}

			absVal := int64(val)
			if absVal < 0 {
				absVal = -absVal
			}

			totalSum += absVal
			if absVal < minAbs {
				minAbs = absVal
			}
		}
	}

	if negCount%2 == 0 {
		return totalSum
	}

	return totalSum - 2*minAbs
}

func main() {
	runTest := func(testNum int, matrix [][]int, expected int64) {
		// Deep copy matrix to avoid mutation side effects
		matrixCopy := make([][]int, len(matrix))
		for i := range matrix {
			matrixCopy[i] = make([]int, len(matrix[i]))
			copy(matrixCopy[i], matrix[i])
		}

		result := maxMatrixSum(matrixCopy)

		status := "FAIL"
		if reflect.DeepEqual(result, expected) {
			status = "PASS"
		}

		fmt.Printf("Test Case %d: %d (Expected: %d) -> %s\n",
			testNum, result, expected, status)
	}

	// Example 1
	matrix1 := [][]int{
		{1, -1},
		{-1, 1},
	}
	runTest(1, matrix1, 4)

	// Example 2
	matrix2 := [][]int{
		{1, 2, 3},
		{-1, -2, -3},
		{1, 2, 3},
	}
	runTest(2, matrix2, 16)

	// Edge Case: Single negative smallest value
	matrix3 := [][]int{
		{5, 5},
		{5, -1},
	}
	runTest(3, matrix3, 14)

	// All negatives, odd count
	matrix4 := [][]int{
		{-1, -2},
		{-3, -4},
	}
	// abs sum = 10, min abs = 1, odd negatives → 10 - 2 = 8
	runTest(4, matrix4, 10)
}
