from collections import deque


class TreeNode(object):

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def createBinaryTree(self, descriptions):
        nodes = {}
        children = set()

        for parent_val, child_val, is_left in descriptions:
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)

            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)

            children.add(child_val)

            if is_left == 1:
                nodes[parent_val].left = nodes[child_val]
            else:
                nodes[parent_val].right = nodes[child_val]

        for val, node in nodes.items():
            if val not in children:
                return node

        return None


def tree_to_list(root):
    """Helper function to serialize tree to LeetCode's array format."""
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Clean up trailing Nones to match LeetCode output exactly
    while result and result[-1] is None:
        result.pop()

    return result


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, descriptions, expected):
        root = solver.createBinaryTree(descriptions)
        result = tree_to_list(root)

        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Input:    {descriptions}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    run_test(
        case_num=1,
        descriptions=[[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]],
        expected=[50, 20, 80, 15, 17, 19],
    )

    # Example 2
    run_test(
        case_num=2,
        descriptions=[[1, 2, 1], [2, 3, 0], [3, 4, 1]],
        expected=[1, 2, None, None, 3, 4],
    )
