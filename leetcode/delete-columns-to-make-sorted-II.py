class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        N = len(strs)
        M = len(strs[0])

        is_sorrted = [False] * (N - 1)
        delete_count = 0

        for col in range(M):
            must_delete = 0

            for i in range(N - 1):
                if not is_sorrted[i]:
                    if strs[i][col] > strs[i + 1][col]:
                        must_delete = True
                        break
        
            if must_delete:
                delete_count += 1
            
            else:

                for i in range(N - 1):
                    if not is_sorrted[i]:
                        if strs[i][col] < strs[i + 1][col]:
                            is_sorrted[i] = True
        
        return delete_count
    

if __name__ == "__main__":
    solver = Solution()

    # Test Case 1
    # Col 0: 'c', 'b', 'a' -> Not sorted (c > b). Delete.
    # Col 1: 'a', 'b', 'c' -> Sorted. Keep.
    # Result: ["a", "b", "c"] is sorted. Total deletions: 1.
    strs1 = ["ca","bb","ac"]
    print(f"Test Case 1: {solver.minDeletionSize(strs1)} (Expected: 1)")

    # Test Case 2
    # Already sorted: "xc" < "yb" < "za". No deletions needed.
    strs2 = ["xc","yb","za"]
    print(f"Test Case 2: {solver.minDeletionSize(strs2)} (Expected: 0)")

    # Test Case 3
    # Col 0: z > w (Delete)
    # Col 1: y > v (Delete)
    # Col 2: x > u (Delete)
    # All columns break order.
    strs3 = ["zyx","wvu","tsr"]
    print(f"Test Case 3: {solver.minDeletionSize(strs3)} (Expected: 3)")