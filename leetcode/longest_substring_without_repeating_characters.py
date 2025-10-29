class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        char_set = set()
        l_ptr = 0
        result = 0

        for r_ptr in range(len(s)):
            while s[l_ptr] in char_set:
                char_set.remove(s[l_ptr])
                l_ptr += 1
            char_set.add(s[r_ptr])
            result = max(result, r_ptr - l_ptr + 1)
        return result