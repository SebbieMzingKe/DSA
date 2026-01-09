# binary tree defn

from collections import deque


class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        def dfs(node):
            if not node:
                return None, 0
            
            left_node, left_depth = dfs(node.left)
            right_node, right_depth = dfs(node.right)

            if left_depth > right_depth:
                return left_node, left_depth + 1
            
            elif left_depth < right_depth:
                return right_node, right_depth + 1

            else:
                return node, left_depth + 1
        
        result_node, _ = dfs(root)
        return result_node
            

def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while deque and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)

        i += 1
    
    return root

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, values, expected_val):
        root = build_tree(values)
        result_node = solver.subtreeWithAllDeepest(root)
        
        result_val = result_node.val if result_node else None
        
        status = "PASS" if result_val == expected_val else "FAIL"
        print(f"Test Case {case_num}: Output Node Val = {result_val} (Expected: {expected_val}) -> {status}")

    # Example 1
    # Deepest nodes are 7 and 4 (depth 3).
    # Their lowest common ancestor is 2.
    # Tree: [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]
    run_test(1, [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 2)
    
    # Example 2
    # Only one node.
    run_test(2, [1], 1)
    
    # Example 3
    # Deepest node is 2 (depth 2). Smallest subtree containing it is just [2].
    # Tree: [0, 1, 3, null, 2]
    run_test(3, [0, 1, 3, None, 2], 2)