package main

// import (
// 	"fmt"
// 	"reflect"
// )

// func plusOne(digits []int) []int {
// 	for i := len(digits) - 1; i >= 0; i-- {
// 		if digits[i] < 9 {
// 			digits[i]++
// 			return digits
// 		}
// 		digits[i] = 0
// 	}	

// 	return append([]int{1}, digits...)
// }

// func main() {
// 	runTest := func(testNum int, input []int, expected []int) {
// 		inputCopy := make([]int, len(input))
// 		copy(inputCopy, input)
		
// 		result := plusOne(inputCopy)
		
// 		status := "FAIL"
// 		if reflect.DeepEqual(result, expected) {
// 			status = "PASS"
// 		}

// 		fmt.Printf("Test Case %d: %v (Expected: %v) -> %s\n", testNum, result, expected, status)
// 	}

// 	// Example 1
// 	digits1 := []int{1, 2, 3}
// 	expected1 := []int{1, 2, 4}
// 	runTest(1, digits1, expected1)

// 	// Example 2
// 	digits2 := []int{4, 3, 2, 1}
// 	expected2 := []int{4, 3, 2, 2}
// 	runTest(2, digits2, expected2)

// 	digits3 := []int{9}
// 	expected3 := []int{1, 0}
// 	runTest(3, digits3, expected3)
	
// 	digits4 := []int{9, 9, 9}
// 	expected4 := []int{1, 0, 0, 0}
// 	runTest(4, digits4, expected4)
// }