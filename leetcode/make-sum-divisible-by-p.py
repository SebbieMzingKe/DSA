class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """

        # Find what remainder we need to remove
        target = sum(nums) % p

        if target == 0:
            return 0
        
        # Map: (prefix_sum % p) -> index
        # Initialize with 0: -1 to handle removing a prefix
        seen = {0: -1}

        for i, num in enumerate(nums):
            # Update running prefix sum (mod p)
            curr_sum = (curr_sum + num) % p

            # We need: (curr_sum - prev_sum) % p == target
            # So: prev_sum % p == (curr_sum - target) % p
            needed = (curr_sum - target + p) % p

            if needed in seen:
                # found a valid sub array to remove
                min_len = min(min_len, i - seen[needed])

            # store current prefix sum
            seen[curr_sum] = i

        # if unable toremove the entire array
        return -1 if min_len == len(nums) else min_len