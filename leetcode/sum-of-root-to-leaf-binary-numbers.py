from collections import deque

class Solution(object):
    def sumRootToLeaf(self, root):

        def dfs(node, current_val):
            if not node:
                return 0
            
            current_val = current_val << 1 | node.val

            if not node.left and not node.right:
                return current_val

            return dfs(node.left, current_val) + dfs(node.right, current_val)
        return dfs(root, 0)


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        # Left child
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # Right child
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, values, expected):
        root = build_tree(values)
        result = solver.sumRootToLeaf(root)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test Case {case_num}: Input {values} -> {result} (Expected: {expected}) -> {status}"
        )

    # Example 1
    # Paths:
    # 1->0->0 = 4
    # 1->0->1 = 5
    # 1->1->0 = 6
    # 1->1->1 = 7
    # Sum = 22
    run_test(1, [1, 0, 1, 0, 1, 0, 1], 22)

    # Example 2
    # Single node 0 -> 0
    run_test(2, [0], 0)

    # Custom Case: Single node 1
    # Path: 1 -> 1
    run_test(3, [1], 1)

    # Custom Case: Unbalanced tree
    #     1
    #    / \
    #   0   None
    #  / \
    # 1   1
    # Paths: 1->0->1 (5), 1->0->1 (5). Sum = 10
    run_test(4, [1, 0, None, 1, 1], 10)
