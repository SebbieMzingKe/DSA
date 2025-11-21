class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0

        for char in set(s):
            first = s.index(char)
            last = s.rindex(char)

            if first < last:
                result += len(set(s[first + 1:last]))

        return result