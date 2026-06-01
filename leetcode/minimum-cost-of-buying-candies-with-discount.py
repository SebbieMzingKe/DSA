class Solution(object):
    def minimumCost(self, cost):
        cost.sort(reverse=True)
        total_cost = 0

        for i in range(len(cost)):
            if (i + 1) % 3 != 0:
                total_cost += cost[i]
        return total_cost


if __name__ == "__main__":
    solver = Solution()

    def run_test(case_num, cost, expected):
        # Pass a copy cost[:] so printing displays the original un-mutated list
        result = solver.minimumCost(cost[:])
        status = "PASS" if result == expected else "FAIL"

        print(f"Test Case {case_num}:")
        print(f"  Input costs: {cost}")
        print(f"  Output:      {result}")
        print(f"  Expected:    {expected}")
        print(f"  Status:      {status}\n")

    # Example 1
    run_test(1, [1, 2, 3], 5)

    # Example 2
    run_test(2, [6, 5, 7, 9, 2, 2], 23)

    # Example 3
    run_test(3, [5, 5], 10)

    # Custom Case 4: Perfect multiple of 3
    run_test(4, [10, 10, 10], 20)
