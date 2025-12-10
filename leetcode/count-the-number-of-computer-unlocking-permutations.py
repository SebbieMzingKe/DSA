class Solution(object):
    def countPermutations(self, complexity):
        """
        :type complexity: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(complexity)
        
        # Constraint Check: The root (index 0) must be the unique minimum.
        # If any computer has complexity <= root, it cannot be unlocked 
        # because the dependency chain must strictly decrease back to the root.
        root_val = complexity[0]
        for i in range(1, n):
            if complexity[i] <= root_val:
                return 0
        
        # If the condition holds, 0 can unlock everyone directly.
        # We just need to permute the remaining n-1 elements.
        # Result is (n-1)! % MOD
        ans = 1
        for i in range(2, n): # Loop calculates 1 * 2 * ... * (n-1)
            ans = (ans * i) % MOD
            
        return ans