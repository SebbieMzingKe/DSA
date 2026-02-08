import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        def check_height(node):
            if not node: return 0
            
            left_h = check_height(node.left)
            if left_h == -1: return -1
            
            right_h = check_height(node.right)
            if right_h == -1: return -1
            
            if abs(left_h - right_h) > 1: return -1
            
            return 1 + max(left_h, right_h)

        return check_height(root) != -1

# --- Helper to build tree from list (LeetCode format) ---
def build_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = collections.deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Left Child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right Child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
        
    return root

if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, values, expected):
        root = build_tree(values)
        result = solver.isBalanced(root)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: {values} -> {result} (Expected: {expected}) -> {status}")

    # Example 1
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    # Left height: 1 (node 9)
    # Right height: 2 (node 20 -> 15/7)
    # Diff is 1. Balanced.
    run_test(1, [3,9,20,None,None,15,7], True)

    # Example 2
    #         1
    #        / \
    #       2   2
    #      / \
    #     3   3
    #    / \
    #   4   4
    # Left height: 3 (1->2->3->4)
    # Right height: 1 (1->2)
    # Diff is 2. Unbalanced.
    run_test(2, [1,2,2,3,3,None,None,4,4], False)

    # Example 3: Empty tree
    run_test(3, [], True)
    
    # Custom Case: Single skew left (Unbalanced)
    # 1 -> 2 -> 3
    run_test(4, [1,2,None,3,None], False)