package main

import "fmt"

type TreeNode struct {
	val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxProduct(root *TreeNode) int {
	const MOD int64 = 1_000_000_007

	var subtreeSums []int64

	var dfs func(node *TreeNode) int64

	dfs = func(node *TreeNode) int64 {
		if node == nil {
			return 0
		}

		sum := int64(node.val) + dfs(node.Left) + dfs(node.Right)
		subtreeSums = append(subtreeSums, sum)
		return sum
	}

	totalSum := dfs(root)

	var maxProduct int64 = 0
	for _, s := range subtreeSums {
		product := s * (totalSum - s)
		if product > maxProduct {
			maxProduct = product
		}
	}

	return int(maxProduct % MOD)
}

func buildTree(values []*int) *TreeNode {
	if len(values) == 0 || values[0] == nil {
		return nil
	}

	root := &TreeNode{val: *values[0]}
	queue := []*TreeNode{root}

	i := 1

	for len(queue) > 0 && i < len(values) {
		node := queue[0]
		queue = queue[1:]

		if i < len(values) && values[i] != nil {
			node.Left = &TreeNode{val: *values[i]}
			queue = append(queue, node.Left)
		}
		i++

		if i < len(values) && values[i] != nil {
			node.Right = &TreeNode{val: *values[i]}
			queue = append(queue, node.Right)
		}
		i++
	}

	return root
}

func runTest(testNum int, values []*int, expected int) {
	root := buildTree(values)
	result := maxProduct(root)

	status := "FAIL"
	if result == expected {
		status = "PASS"
	}

	fmt.Printf("Test Case %d: %d (Expected: %d) -> %s\n",
		testNum, result, expected, status)
}

// -------- 5. Main --------
func main() {
	// Helper to create *int
	ptr := func(v int) *int { return &v }

	// Example 1
	runTest(1,
		[]*int{ptr(1), ptr(2), ptr(3), ptr(4), ptr(5), ptr(6)},
		110,
	)

	// Example 2
	runTest(2,
		[]*int{ptr(1), nil, ptr(2), ptr(3), ptr(4), nil, nil, ptr(5), ptr(6)},
		90,
	)
}
