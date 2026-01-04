import math


class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total_sum = 0
        
        for num in nums:
            if num < 6: 
                continue
                
            div_sum = 0
            count = 0
            limit = int(math.sqrt(num))
            
            for i in range(1, limit + 1):
                if num % i == 0:
                    if i * i == num:
                        count += 1
                        div_sum += i
                    else:
                        count += 2
                        div_sum += i + (num // i)
                    
                    if count > 4:
                        break
            
            if count == 4:
                total_sum += div_sum
                
        return total_sum
    
if __name__ == "__main__":
    solver = Solution()
    
    # Helper function to print results
    def run_test(case_num, nums, expected):
        result = solver.sumFourDivisors(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test Case {case_num}: {result} (Expected: {expected}) -> {status}")

    # Example 1
    # 21: Divisors [1, 3, 7, 21] -> Count 4 -> Sum 32
    # 4:  Divisors [1, 2, 4]     -> Count 3 -> Ignore
    # 7:  Divisors [1, 7]        -> Count 2 -> Ignore
    # Total: 32
    run_test(1, [21, 4, 7], 32)
    
    # Example 2
    # Both 21s contribute 32. Total: 64
    run_test(2, [21, 21], 64)
    
    # Example 3
    # No number has 4 divisors here.
    run_test(3, [1, 2, 3, 4, 5], 0)
    
    # Edge Case: 10 (1, 2, 5, 10) -> Sum 18
    run_test(4, [10], 18)