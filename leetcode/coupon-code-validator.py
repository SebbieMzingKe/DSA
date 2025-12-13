class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """

        priority_map = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }

        valid_coupons = []

        for i in range(len(code)):
            c = code[i]
            b_line = businessLine[i]
            active = isActive[i]

            if not active:
                continue

            if b_line not in priority_map:
                continue

            if not c:
                continue

            is_valid_format = True

            for char in c:

                if not (char.isalnum() or char == '_'):
                    is_valid_format = False
                    break

            if not is_valid_format:
                continue

            valid_coupons.append((priority_map[b_line], c))

        valid_coupons.sort(key=lambda x: (x[0], x[1]))

        return [item[1] for item in valid_coupons]

if __name__ == "__main__":
    solver = Solution()
    
    # Example 1
    code1 = ["SAVE20","","PHARMA5","SAVE@20"]
    bl1 = ["restaurant","grocery","pharmacy","restaurant"]
    act1 = [True,True,True,True]
    print(solver.validateCoupons(code1, bl1, act1)) 
    # Expected: ['PHARMA5', 'SAVE20']

    # Example 2
    code2 = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"]
    bl2 = ["grocery","electronics","invalid"]
    act2 = [False,True,True]
    print(solver.validateCoupons(code2, bl2, act2))
    # Expected: ['ELECTRONICS_50']