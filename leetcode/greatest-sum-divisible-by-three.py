class Solution(object):
    def maxSumDivThree(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        remainder = total % 3

        if remainder == 0:
            return total
        
        rem_one= []
        rem_two = []

        for n in nums:
            if n % 3 == 1:
                rem_one.append(n)
            elif n % 3 == 2:
                rem_two.append(n)
        rem_one.sort()
        rem_two.sort()
            
        if remainder == 1:
            option_one = rem_one[0] if rem_one else float("inf")
            option_two = rem_two[0] + rem_two[1] if len(rem_two) >= 2 else float("inf")
            return total - min(option_one, option_two)
        
        else:
            option_one = rem_two[0] if rem_two else float("inf")
            option_two = rem_one[0] + rem_one[1] if len(rem_one) >= 2 else float("inf")
            return total - min(option_one, option_two)