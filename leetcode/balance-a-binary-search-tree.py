class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def balanceBST(self, root):
        sorted_vals = []

        def inorder_dfs(node):
            if not node:
                return
            inorder_dfs(node.left)
            sorted_vals.append(node.val)
            inorder_dfs(node.right)

        inorder_dfs(root)

        def build_tree(start, end):
            if start > end:
                return None

            mid = (start + end) // 2

            node = TreeNode(sorted_vals[mid])
            node.left = build_tree(start, mid - 1)
            node.right = build_tree(mid + 1, end)

            return node

        return build_tree(0, len(sorted_vals) - 1)


def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root


def get_height(node):
    if not node:
        return 0
    return 1 + max(get_height(node.left), get_height(node.right))


def is_balanced(node):
    if not node:
        return True
    lh = get_height(node.left)
    rh = get_height(node.right)
    return abs(lh - rh) <= 1 and is_balanced(node.left) and is_balanced(node.right)


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, values):
        root = None
        for v in values:
            root = insert_into_bst(root, v)

        new_root = solver.balanceBST(root)

        balanced = is_balanced(new_root)
        status = "PASS" if balanced else "FAIL"

        h = get_height(new_root)
        print(
            f"Test Case {case_num}: Input {values} -> Height {h} -> Balanced? {balanced} -> {status}"
        )

    # Example 1: [1, 2, 3, 4] inserted sequentially creates a skewed tree (height 4)
    # Balanced height should be ~3
    run_test(1, [1, 2, 3, 4])

    # Example 2: [2, 1, 3] already balanced
    run_test(2, [2, 1, 3])

    # Custom: Larger skewed tree
    run_test(3, list(range(1, 16)))  # 1 to 15, should become height 4
