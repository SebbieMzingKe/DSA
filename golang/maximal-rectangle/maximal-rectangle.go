package main


import (
	"fmt"
)

func maximalRectangle(matrix [][]byte) int {
	if len(matrix) == 0 {
		return 0
	}
	cols := len(matrix[0])
	heights := make([]int, cols)
	maxArea := 0

	for _, row := range matrix {
		for j, val := range row {
			if val == '1' {
				heights[j]++
			} else {
				heights[j] = 0
			}
		}
		currentArea := largestRectangleArea(heights)
		if currentArea > maxArea {
			maxArea = currentArea
		}
	}
	return maxArea
}

func largestRectangleArea(heights []int) int {
	stack := []int{-1}
	maxArea := 0
	for i := 0; i <= len(heights); i++ {
		currentH := 0
		if i < len(heights) {
			currentH = heights[i]
		}
		for len(stack) > 1 && currentH < heights[stack[len(stack)-1]] {
			h := heights[stack[len(stack)-1]]
			stack = stack[:len(stack)-1]
			w := i - stack[len(stack)-1] - 1
			if h*w > maxArea {
				maxArea = h*w
			}
		}
		stack = append(stack, i)
	}
	return maxArea
}

func main() {
	makeMatrix := func(rows []string) [][]byte {
		mat := make([][]byte, len(rows))
		for i, s := range rows {
			mat[i] = []byte(s)
		}
		return mat
	}

	runTest := func(testNum int, input []string, expected int) {
		matrix := makeMatrix(input)
		result := maximalRectangle(matrix)
		status := "FAIL"
		if result == expected {
			status = "PASS"
		}
		fmt.Printf("Test Case %d: Expected %d, Got %d -> %s\n", testNum, expected, result, status)
	}

	input1 := []string{
		"10100",
		"10111",
		"11111",
		"10010",
	}
	runTest(1, input1, 6)

	input2 := []string{"0"}
	runTest(2, input2, 0)

	input3 := []string{"1"}
	runTest(3, input3, 1)

	input4 := []string{
		"11",
		"11",
	}
	runTest(4, input4, 4)
}