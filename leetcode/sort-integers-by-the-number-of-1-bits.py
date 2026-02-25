class Solution(object):
    def sortByBits(self, arr):

        arr.sort(key = lambda x :(bin(x).count("1"), x))

        return arr


if __name__ == "__main__":
    solver = Solution()
    
    def run_test(case_num, arr, expected):
        result = solver.sortByBits(arr[:])
        status = "PASS" if result == expected else "FAIL"
        
        print(f"Test Case {case_num}:")
        print(f"  Input:    {arr}")
        print(f"  Output:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status:   {status}\n")

    # Example 1
    # 0 -> 0 bits
    # 1, 2, 4, 8 -> 1 bit
    # 3, 5, 6 -> 2 bits
    # 7 -> 3 bits
    run_test(1, [0,1,2,3,4,5,6,7,8], [0,1,2,4,8,3,5,6,7])

    # Example 2
    # Powers of 2 all have exactly 1 bit. 
    # They should just be sorted by their actual values.
    run_test(2, [1024,512,256,128,64,32,16,8,4,2,1], [1,2,4,8,16,32,64,128,256,512,1024])

    # Custom Case: Duplicate values
    run_test(3, [10, 10, 3, 3], [3, 3, 10, 10])
    
    # Custom Case: Same bit counts, distinct large numbers
    # 15 (1111) -> 4 bits, 23 (10111) -> 4 bits
    run_test(4, [23, 15], [15, 23])